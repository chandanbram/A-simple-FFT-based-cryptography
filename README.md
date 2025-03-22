# **FFT-Based Cryptography: Secure Data Transmission Using Socket Programming**

## Overview
This project implements **secure data encryption and decryption** using the **Fast Fourier Transform (FFT)**. Messages are transformed into the frequency domain, encrypted, sent over a network, and decrypted using the **Inverse FFT (IFFT)**. It ensures **secure communication** without relying on built-in cryptographic functions. A **custom FFT implementation** is used instead of built-in FFT functions. Additionally, a **TCP-based two-way chat system** is provided for **interactive encrypted communication**.

## **\ud83d\udcc2 Project Structure**
```
FFT_Cryptography/
│── encryptor.py         # Encrypts and sends the message
│── decrypter.py         # Receives and decrypts the message
│── fft_cryptography.py  # (Optional) Two-way communication using TCP sockets
│── README.md            # Project documentation
```

## **How It Works**
1. **Encryption (Sender)**:
   - Converts the message to a **numerical signal (ASCII values)**.
   - Applies **custom FFT** to transform it into the frequency domain.
   - Encrypts the signal by modifying frequency components with a **random key**.
   - Sends the encrypted data over a network using **sockets**.
2. **Decryption (Receiver)**:
   - Receives the encrypted data via **socket communication**.
   - Applies **custom Inverse FFT (IFFT)** to reconstruct the original message.
   - Prints the decrypted message.
3. **Optional: Two-Way Secure Chat**:
   - The **fft_cryptography.py** file enables **real-time encrypted messaging**.
   - No predefined sender or receiver—users can dynamically switch roles.
   - Uses **TCP for stable, two-way communication**.

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
## **Usage**
### **Option 1: One-Way Communication (Encryptor & Decrypter)**
#### **Run the Receiver (Decrypter) First**
Start the **decryption server** (must be running before the sender):
```bash
python3 decrypter.py
```
#### **Run the Sender (Encryptor)**
Open another terminal and run:
```bash
python3 encryptor.py
```
Enter a message to encrypt and send.
#### **Check the Receiver Output**
After receiving the encrypted message, the receiver will **decrypt and display the original message**.

### **Option 2: Two-Way Communication Using TCP**
This mode allows **both users to send and receive messages** dynamically. **No predefined roles**—users can choose to send or receive at any time.
#### **Start the First User**
Run:
```bash
python3 fft_cryptography.py
```
If no server is found, this instance will **automatically start as the server**.
#### **Start the Second User**
Run:
```bash
python3 fft_cryptography.py
```
This instance will **automatically connect as a client**.
#### **Send and Receive Messages**
Once connected, both users can **send and receive messages** continuously.

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
### **Two-Way Communication (fft_cryptography.py)**
#### **User 1 (Server)**
```
FFT-Based Secure Communication
Connected to ('127.0.0.1', 54321)
Press 'S' to Send a message, 'R' to Receive a message, or 'Q' to Quit: S
Enter your message: Hi there
Message sent securely!
```
#### **User 2 (Client)**
```
FFT-Based Secure Communication
Connected to the server at 127.0.0.1:3000
Press 'S' to Send a message, 'R' to Receive a message, or 'Q' to Quit: R
Received Encrypted Message: [Encrypted Data]
Decrypted Message: Hi there
```

## **Key Features**
✅ **No inbuilt FFT functions used** – A custom **recursive FFT and IFFT** is implemented in fft_cryptography.
✅ **Both one-way and two-way communication**.
✅ **TCP-based version provides stable, full-duplex messaging**.
✅ **Ensures message security by encrypting frequency components**.

## **Conclusion**
This project demonstrates how **FFT-based cryptography** can be used for **secure messaging**.
- The **Encryptor-Decrypter** setup is ideal for **one-way secure messaging**.
- The **TCP-based alternative** enables **bi-directional encrypted communication**.

Now, your **secure FFT-based communication system** is ready to use!

