# 🧠 Python HTTP Web Server with Middleware & TLS

**This is a simple, multithreaded HTTP web server built using Python socket programming**, with support for:

* 🌐 Basic routing
* ⚙️ Middleware (logging, security, authentication)
* 🔐 Optional HTTPS via TLS (SSL)

---

## 🚀 Features

* ✅ **Threaded client handling**
* ✅ **Routes** for `/`, `/about`, `/admin`, `/contact`, `/api/info`
* ✅ **Custom HTML pages** with CSS
* ✅ **Middleware**:

  * Logging IP, method, and path
  * Blocking specific IPs or disallowed HTTP methods
  * Token-based authentication middleware
* ✅ **HTTPS support** with self-signed certificate

---

## 🗂️ Project Structure

```bash
.
├── server.py           # Main threaded HTTP server
├── routes.py           # Handles HTML route responses
├── middleware.py       # Contains logging, security, TLS, and auth middleware
├── .env                # Stores address and port config
├── cert.pem            # SSL certificate (self-signed)
├── key.pem             # SSL key (self-signed)
└── README.md           # You're reading it!
```

---

## ⚙️ Setup Instructions

### 🔹 1. Clone the repository

```bash
git clone https://github.com/danishnaseer00/HTTP-Server-using-Socket.git
cd HTTP-Server-using-Socket
```

### 🔹 2. Install dependencies

```bash
pip install python-dotenv
```

### 🔹 3. Create `.env` file

```env
Port=8000
Address=0.0.0.0
```

### 🔹 4. (Optional) Generate SSL Cert & Key

```bash
openssl req -new -x509 -keyout key.pem -out cert.pem -days 365 -nodes
```

### 🔹 5. Run the server

```bash
python server.py
```

🧪 Open browser:

* **HTTP**: `http://localhost:8080/`
* **HTTPS**: `https://localhost:8080/` *(you'll get a browser warning — accept for testing)*

---


## ✍️ Author

Built by **Danish Naseer** — learning web server development from scratch with Python.

