import numpy as np
import socket
import pickle
import threading
import struct
import cmath

print("FFT-Based Secure Communication")

HOST = "127.0.0.1"
PORT = 3000  # Single port for both sending and receiving

# --- FFT Encryption & Decryption Functions ---

def next_power_of_2(n):
    """ Find the next power of 2 (for FFT optimization). """
    return 1 if n == 0 else 2**(n - 1).bit_length()

def message_to_polynomial(message):
    """ Convert message to a large polynomial (ASCII values). """
    poly = [ord(char) for char in message]
    n = max(1024, next_power_of_2(len(poly)))  # Ensure at least 1024 coefficients
    poly += [0] * (n - len(poly))  # Zero-padding
    return np.array(poly, dtype=np.float64)  # Use float64 for precision

def fft(poly):
    """ Custom Recursive FFT for Large Polynomials """
    n = len(poly)
    if n == 1:
        return poly
    even = fft(poly[0::2])
    odd = fft(poly[1::2])
    factor = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + factor[k] for k in range(n // 2)] + [even[k] - factor[k] for k in range(n // 2)]

def ifft(poly):
    """ Custom Recursive IFFT for Large Polynomials """
    n = len(poly)
    if n == 1:
        return poly
    even = ifft(poly[0::2])
    odd = ifft(poly[1::2])
    factor = [cmath.exp(2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    result = [even[k] + factor[k] for k in range(n // 2)] + [even[k] - factor[k] for k in range(n // 2)]
    return [x / 2 for x in result]  # Normalize

def encrypt_fft(message):
    """ Encrypt a message using FFT with a large polynomial. """
    poly = message_to_polynomial(message)
    transformed_poly = fft(poly)
    key = np.random.rand(len(poly))  # Generate large random key
    encrypted_poly = [transformed_poly[i] * key[i] for i in range(len(poly))]
    return encrypted_poly, key

def decrypt_fft(encrypted_poly, key):
    """ Decrypt a message using IFFT. """
    decrypted_poly = [encrypted_poly[i] / key[i] for i in range(len(encrypted_poly))]
    recovered_poly = ifft(decrypted_poly)
    recovered_poly = [x.real for x in recovered_poly]
    return ''.join(chr(int(num)) for num in np.round(recovered_poly) if num > 0)

# --- Establish Connection Automatically ---
def establish_connection():
    """ Tries to connect as a client first, otherwise starts as a server. """
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")
        return client_socket  # Returns the connected socket
    except ConnectionRefusedError:
        print(f"Starting as server on PORT {PORT}...")
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        conn, addr = server_socket.accept()
        print(f"Connected to {addr}")
        return conn  # Returns the connected socket

# --- Two-Way Communication Function ---
def handle_communication(sock):
    """ Allows both users to send and receive messages. """
    while True:
        try:
            choice = input("\nPress 'S' to Send a message, 'R' to Receive a message, or 'Q' to Quit: ").strip().lower()

            if choice == "s":
                send_message(sock)
            elif choice == "r":
                receive_message(sock)
            elif choice == "q":
                print("Exiting chat.")
                sock.close()
                break
            else:
                print("Invalid choice. Please press 'S', 'R', or 'Q'.")
        except Exception as e:
            print(f"Connection lost: {e}")
            break

# --- Send Message Function ---
def send_message(sock):
    """ Encrypts and sends a message. """
    message = input("\nEnter your message (or type 'exit' to quit): ").strip()
    if message.lower() == "exit":
        print("Exiting sender mode.")
        return

    encrypted_message, key = encrypt_fft(message)
    packet = pickle.dumps((encrypted_message, key))  # Serialize using pickle

    # Send message length first (to prevent truncation issues)
    msg_length = struct.pack("!I", len(packet))  
    sock.sendall(msg_length)  # Send the length first
    sock.sendall(packet)  # Send the actual message

    print("Message sent securely!")

# --- Receive Message Function ---
def receive_message(sock):
    """ Receives and decrypts a message. """
    try:
        # First, receive the message length
        msg_length_data = sock.recv(4)  
        if not msg_length_data:
            print("Connection closed by the other user.")
            return

        msg_length = struct.unpack("!I", msg_length_data)[0]  # Unpack the length
        data = b""

        # Keep receiving until the full message is obtained
        while len(data) < msg_length:
            chunk = sock.recv(msg_length - len(data))
            if not chunk:
                print("Connection lost.")
                return
            data += chunk

        encrypted_message, key = pickle.loads(data)  # Deserialize

        # Show encrypted message
        print(f"\nReceived Encrypted Message: {encrypted_message[:10]}... (truncated)")

        # Decrypt message
        decrypted_message = decrypt_fft(encrypted_message, key)
        print(f"Decrypted Message: {decrypted_message}")

    except Exception as e:
        print(f"Error while receiving message: {e}")

# --- Main Function ---
def main():
    sock = establish_connection()  # Automatically connect as client or start as server
    handle_communication(sock)  # Start communication loop

if __name__ == "__main__":
    main()