# 📄 Resume Analyzer

An AI-powered Resume Analyzer built with Django and Groq AI that analyzes resumes and provides ATS score with detailed feedback.

---

## 📌 About The Project

Upload your resume and get instant AI-powered analysis including:
- ATS Score out of 100
- Strong points
- Missing keywords
- Improvements needed
- Overall feedback

---

## 🚀 Features

- ✅ PDF and Word resume support
- ✅ AI powered analysis using Groq AI
- ✅ Real ATS Score
- ✅ Color coded score (Green/Yellow/Red)
- ✅ Detailed feedback
- ✅ Beautiful responsive UI

---

## ⚙️ Technologies Used

| Frontend | Backend | AI | Database |
|---|---|---|---|
| HTML, CSS | Python, Django | Groq AI (LLaMA) | SQLite |
| Bootstrap 5 | | | |

---

## 🛠️ How To Run

### 1. Clone the repository
git clone https://github.com/shradham-13/Resume_Analyzer.git

### 2. Go to project folder
cd Resume_Analyzer

### 3. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 4. Install packages
pip install -r requirements.txt

### 5. Add your Groq API key in .env file
GROQ_API_KEY=your-api-key-here

### 6. Run migrations
python manage.py migrate

### 7. Start server
python manage.py runserver

### 8. Open in browser
http://127.0.0.1:8000

---

## 👩‍💻 Developer

Made by Shradha Madane
