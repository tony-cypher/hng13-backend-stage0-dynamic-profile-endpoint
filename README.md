# 🐍 HNG13 Backend Stage 0 — Dynamic Profile API

A simple yet production-ready **FastAPI** application that returns developer profile information along with a **dynamic cat fact** fetched from an external API.

This project is built as part of the **HNG13 Backend Internship** challenge — Stage 0 task.

---

## 🚀 Features

- ✅ Built with **FastAPI** (Python 3.10+)
- 🕒 Returns **current UTC timestamp** (ISO 8601 format)
- 🐈 Fetches a **random cat fact** dynamically from [catfact.ninja](https://catfact.ninja/)
- 🔐 Uses **environment variables** for configuration
- 🌍 Supports **CORS** for frontend access
- ⚙️ Includes **logging** for debugging
- 🧢 Optional **rate limiting** for public deployments (via `slowapi`)

---

## 📁 Project Structure

```
.
├── src/                 # Main FastAPI application
│   ├── config.py        # Configuration settings
│   └── main.py          # FastAPI entry point
├── .env                 # Environment variables (not committed)
├── .gitignore           # Git ignore rules
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

---

## ⚙️ Requirements

- Python 3.10 or newer  
- pip (Python package manager)  

---

## 🧩 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/tony-cypher/hng13-backend-stage0-dynamic-profile-endpoint.git
cd hng13-backend-stage0-dynamic-profile-endpoint
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` file in the project root

```bash
# .env
CONTACT_EMAIL=youremail@gmail.com
```

### 5️⃣ Run the FastAPI server

```bash
python -m uvicorn src.main:app --reload
```

Then open your browser at:

👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

FastAPI doc:

👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧠 API Endpoints

### **Root Endpoint**
**`GET /`**

Returns a short motivational message.

**Example Response:**
```json
{
  "message": "Journey to becoming a finalist begins with this task."
}
```

---

### **Profile Endpoint**
**`GET /me`**

Returns user profile details, a dynamic cat fact, and the current UTC timestamp.

**Example Response:**
```json
{
  "status": "success",
  "user": {
    "email": "tonycypher0@gmail.com",
    "name": "Anaeto Anthony Ifeanyi",
    "stack": "Python/FastAPI, Javascript/NodeJS, TypeScript/NESTJS"
  },
  "timestamp": "2025-10-17T09:30:26Z",
  "fact": "Cats sleep for about 70% of their lives."
}
```

---

## 🌍 Environment Variables

| Variable | Description | Example |
|-----------|-------------|----------|
| `CONTACT_EMAIL` | Developer’s contact email | `tonycypher0@gmail.com`
---

## 🧾 Logging

Logs are printed to the console in the format:

```
2025-10-17 09:32:45,123 [INFO] app: /me endpoint accessed by 127.0.0.1
```

Useful for debugging API access and network errors.

---

## ⏱️ Rate Limiting

This project uses [slowapi](https://pypi.org/project/slowapi/) to prevent abuse.

| Endpoint | Limit |
|-----------|--------|
| `/` | 10 requests per minute |
| `/me` | 5 requests per minute |

You can adjust these limits in `app.py`.

---

## 🧪 Example with `curl`

```bash
curl http://127.0.0.1:8000/me
```

**Response:**
```json
{
  "status": "success",
  "user": {
    "email": "tonycypher0@gmail.com",
    "name": "Anaeto Anthony Ifeanyi",
    "stack": "Python/FastAPI, Javascript/NodeJS, TypeScript/NESTJS"
  },
  "timestamp": "2025-10-17T09:30:26Z",
  "fact": "Cats purr to communicate contentment and calmness."
}
```

## 🧑‍💻 Author

**Name:** Anaeto Anthony Ifeanyi  
**Email:** [tonycypher0@gmail.com](mailto:tonycypher0@gmail.com)  
**Stack:** Python/FastAPI • JavaScript/NodeJS • TypeScript/NestJS

---

## 🏁 License

This project is open-source under the **MIT License**.  
Feel free to fork and improve!

---

## 💡 Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [httpx](https://www.python-httpx.org/)
- [slowapi](https://pypi.org/project/slowapi/)
- [catfact.ninja](https://catfact.ninja/)
- [HNG Internship](https://hng.tech/)

---

> “Journey to becoming a finalist begins with this task.” 🏆
