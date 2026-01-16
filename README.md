# Python TCP Port Scanner

A beginner-friendly TCP port scanner written in Python.  
This tool scans a target IP address to identify open TCP ports within a given range.

---

## 🚀 Features
- Scans a user-defined port range
- Detects open TCP ports
- Shows scan progress
- Displays scan summary
- Handles errors safely
- Clean and beginner-friendly code

---

## 🛠️ Technologies Used
- Python 3
- Socket Programming
- TCP/IP Networking

---

## 📖 How It Works (Simple Explanation)

The scanner tries to create a TCP connection to each port on the target system.

- If the connection is successful → the port is **OPEN**
- If the connection fails or times out → the port is **CLOSED or FILTERED**

This method is commonly used in network reconnaissance and security testing.

---

## ▶️ How to Run

```bash
python port_scanner.py

Enter target IP address: 127.0.0.1
Enter start port: 1
Enter end port: 1024

🔐 Security Concepts Demonstrated

Port scanning

Service discovery

Attack surface analysis

Defensive security awareness

Basic network reconnaissance

⚠️ Disclaimer

This project is created for educational purposes only.
Scan only systems you own or have explicit permission to test.

📌 Future Improvements

Multi-threaded scanning

Service / banner detection

Export results to a file

Faster scanning logic

IPv6 support