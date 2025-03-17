import numpy as np
import socket
import pickle

print("FFT-Based Cryptography")

# Receive encrypted data over the network
def receive_encrypted_data(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Waiting for data...")
        conn, addr = s.accept()
        with conn:
            data = pickle.loads(conn.recv(4096))
            return data  # Return encrypted signal & key

# Decrypt the signal using IFFT
def decrypt_fft(encrypted_signal, key):
    print("Decrypting using Inverse FFT...")
    decrypted_signal = encrypted_signal / key  # Reverse encryption
    recovered_signal = np.fft.ifft(decrypted_signal)  # Apply IFFT
    recovered_signal = np.real(recovered_signal)  # Keep only the real part
    return np.round(recovered_signal).astype(int)  # Convert back to integers

# Run server to receive data
encrypted_signal, key = receive_encrypted_data()
print("Received Encrypted Data:", encrypted_signal)

# Decrypt the message
decrypted_signal = decrypt_fft(encrypted_signal, key)
recovered_message = ''.join(chr(num) for num in decrypted_signal)

print("Decrypted Message:", recovered_message)
