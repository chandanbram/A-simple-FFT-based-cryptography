import numpy as np
import socket
import pickle

print("FFT-Based Cryptography")

# Convert text to numerical signal (ASCII values)
def text_to_signal(message):
    return np.array([ord(char) for char in message], dtype=np.float32)

# Encrypt the signal using FFT
def encrypt_fft(signal):
    print("Encrypting using FFT...")
    transformed_signal = np.fft.fft(signal)  # Apply FFT
    key = np.random.rand(len(signal))  # Generate random key
    encrypted_signal = transformed_signal * key  # Encrypt by modifying frequency components
    return encrypted_signal, key

# Send encrypted data over a network
def send_encrypted_data(encrypted_signal, key, host='127.0.0.1', port=12345):
    print("Sending encrypted data...")
    data = pickle.dumps((encrypted_signal, key))  # Serialize data
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data)
    print("Message sent successfully!")

# Ask user for message
message = input("Enter the message to encrypt: ")
signal = text_to_signal(message)
encrypted_signal, key = encrypt_fft(signal)

send_encrypted_data(encrypted_signal, key)
