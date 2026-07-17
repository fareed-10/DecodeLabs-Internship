# 🔐 Caesar Cipher — Encryption & Decryption Tool

A simple Python program that implements the classic **Caesar Cipher** algorithm to encrypt and decrypt text messages using a shift key.

## 📖 About

The Caesar Cipher is one of the earliest known encryption techniques. Each letter in the message is shifted a fixed number of positions in the alphabet. This project takes user input, encrypts it, and then decrypts it back to verify correctness.

## ⚙️ How It Works

- `encrypt(text, shift)` — shifts each alphabetic character forward by the given key, wrapping around the alphabet (A–Z / a–z). Non-alphabetic characters are left unchanged.
- `decrypt(text, shift)` — reverses the process by shifting characters backward, restoring the original message.

## 🚀 Usage

```bash
python caesar_cipher.py
```

You'll be prompted to enter:
1. Your message
2. A shift key (integer)

The program will then display the original, encrypted, and decrypted message.

**Example:**
```
Enter your message: Hello World
Enter shift key: 3

Original Message : Hello World
Encrypted Message: Khoor Zruog
Decrypted Message: Hello World
```

## 🧠 Concepts Used

- String manipulation
- ASCII / Unicode character codes (`ord`, `chr`)
- Modulo arithmetic for alphabet wraparound
- Basic input/output handling

## 🛠️ Tech Stack

- Python 3

## ✍️ Author

**Fareed** — BS Computer Science, SMIU Karachi
