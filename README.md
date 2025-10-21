🧠 DevLab API — Pure Python Learning Platform

Welcome to DevLab, a minimal backend built entirely with pure Python — no frameworks — to help students learn coding fundamentals and API design from scratch.

🚀 Features

✅ Built with only Python’s standard library (http.server)

✅ Simple JSON-based “database” (data/lessons.json)

✅ REST-like GET routes

/ → Welcome message

/lessons → Returns all lessons

🧱 Clean structure that can evolve into a full learning platform

🗂️ Project Structure
learn_platform/
│
├── server.py           # Main server file
├── data/
│   └── lessons.json    # Mock data file
└── README.md           # Documentation


⚙️ Installation

Clone the repo

git clone https://github.com/<your-username>/DevLab-Backend.git
cd DevLab-Backend


Run the server

python server.py


Open in browser

http://127.0.0.1:8000/
 → Welcome message

http://127.0.0.1:8000/lessons
 → Lesson list

 📘 Example Response
GET /lessons
[
  {
    "id": 1,
    "title": "Python Basics",
    "description": "Introduction to Python for beginners."
  },
  {
    "id": 2,
    "title": "Data Structures",
    "description": "Learn lists, dictionaries, and tuples in Python."
  }
]

💡 Next Steps

🧩 Stage 2 → Add POST endpoint to create new lessons

🔐 Stage 3 → Add users and basic authentication

💾 Stage 4 → Replace JSON with real database (SQLite or MongoDB)

🧑‍💻 Author

Abdulmumini Muhammad Bello
“Learn by doing. Code like a real developer.”
