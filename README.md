# **FFT-Based Cryptography: Secure Data Transmission Using Socket Programming**

## Overview
This project implements **secure data encryption and decryption** using the **Fast Fourier Transform (FFT)**. Messages are transformed into the frequency domain, encrypted, sent over a network, and decrypted using the **Inverse FFT (IFFT)**.

## **📂 Project Structure**
```
FFT_Cryptography/
│── encryptor.py   # Encrypts and sends the message
│── decrypter.py   # Receives and decrypts the message
│── README.md      # Project documentation
```

## **How It Works**
1. **Encryption (Sender)**:
   - Converts the message to a **numerical signal (ASCII values)**.
   - Applies **FFT** to transform it into the frequency domain.
   - Encrypts the signal by modifying frequency components with a random key.
   - Sends the encrypted data over a network using **sockets**.

2. **Decryption (Receiver)**:
   - Receives the encrypted data via **socket communication**.
   - Applies **Inverse FFT (IFFT)** to reconstruct the original message.
   - Prints the decrypted message.

## **Installation & Setup**
### **1️⃣ Install Python**
Ensure **Python 3.x** is installed. Check with:
```bash
python --version
```

### **2️⃣ Install Required Libraries**
Run the following command to install dependencies:
```bash
pip install numpy
```

### **3️⃣ Run the Receiver (Decrypter)**
Start the **decryption server** (must be running before the sender):
```bash
python3 decrypter.py
```

### **4️⃣ Run the Sender (Encryptor)**
Open another terminal and run:
```bash
python3 encryptor.py
```
Enter a message to encrypt and send.

### **5️⃣ Check the Receiver Output**
After receiving the encrypted message, the receiver will **decrypt and display the original message**.

## **Example Output**
### **Sender (encryptor.py)**
```
FFT-Based Cryptography
Enter the message to encrypt: Hello World
Encrypting using FFT...
Sending encrypted data...
Message sent successfully!
```

### **Receiver (decrypter.py)**
```
FFT-Based Cryptography
Waiting for data...
Received Encrypted Data: [...]
Decrypting using Inverse FFT...
Decrypted Message: Hello World
```
