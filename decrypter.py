import numpy as np
import socket
import pickle

# Receive encrypted data over the network
def receive_encrypted_data(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("[SERVER] Waiting for data...")
        conn, addr = s.accept()
        with conn:
            data = pickle.loads(conn.recv(4096))
            return data  

# Decrypt the signal using IFFT
def decrypt_fft(encrypted_signal, key):
    decrypted_signal = encrypted_signal / key  
    recovered_signal = np.fft.ifft(decrypted_signal)  
    return np.round(recovered_signal).astype(int) 

# Run server to receive data
encrypted_signal, key = receive_encrypted_data()
print("[SERVER] Received Encrypted Data:", encrypted_signal)

# Decrypt the message
decrypted_signal = decrypt_fft(encrypted_signal, key)
recovered_message = ''.join(chr(num) for num in decrypted_signal)

print("[SERVER] Decrypted Message:", recovered_message)
