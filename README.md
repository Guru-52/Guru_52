A simple real-time chat application built using Python's socket and threading libraries. It allows multiple clients to connect to a central server and exchange messages over a **local network (LAN)**.

---

## 📦 Features

- Real-time text messaging
- Multi-client support
- Lightweight and terminal-based
- No external dependencies

---

## 🧰 Requirements

- Python 3.x
- All devices must be connected to the **same LAN**
- Basic knowledge of terminal or command prompt

---

## 📁 Project Structure

chat-app/ │ ├── chat_server.py   # Server code ├── chat_client.py   # Client code └── README.md        # This file

---

## 🚀 How to Run

### 1. Run the Server

On the host/server machine:

```bash
python chat_server.py

> This will start the server on all available network interfaces on port 12345.




---

2. Run the Client

On each client machine:

1. Open chat_client.py


2. Update the SERVER_IP variable with the IP address of the server machine.



SERVER_IP = '192.168.1.100'  # Replace with actual server IP

3. Then run:



python chat_client.py

Each client will be prompted to enter their name. Type messages and press Enter to send.


---

🛑 Exiting the Chat

Clients can type exit to leave the chat room gracefully.


---

💡 Example

[Client1 Terminal]
Enter your name: Alice
Alice: Hello everyone!

[Client2 Terminal]
Enter your name: Bob

<output>
Alice has joined the chat.
Alice: Hello everyone!
Bob: Hey Alice!


---

🔒 Notes

Ensure that your firewall or antivirus is not blocking the specified port.

This is a basic educational project and does not include encryption or authentication.



---

🌐 Want a Web Version?

We also offer a web-based version using Flask and WebSockets (via Socket.IO). Contact or request to get the web version code.


---

📜 License

This project is open-source and available under the MIT License.


---

✍️ Author

Your Name – [your-email@example.com]


---

Let me know if you'd like this tailored for a web version, a GUI version (using Tkinter or PyQt), or turned into a GitHub project.

# Guru_52
