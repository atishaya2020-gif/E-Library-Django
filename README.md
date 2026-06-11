# 📚 E-Library Django

A full-stack E-Library web application built using Django that allows users to register, login, upload books, explore available books, and read/download PDFs online.

This project is deployed with a production-ready setup using PostgreSQL, Cloudinary, WhiteNoise, and Render.

---

## 🌐 Live Demo

🔗 https://e-library-django-82z7.onrender.com/

---

## ✨ Features

### 👤 User Authentication
- User registration
- Secure login/logout
- Session management
- User-based book uploads

### 📖 Book Management
- Upload books with:
  - Title
  - Category
  - Number of pages
  - Description
  - PDF file

- Explore uploaded books
- View book details
- Read PDF online
- Download PDF files

### ☁️ Cloud Storage
- Uploaded PDFs are stored permanently using Cloudinary
- Production-safe media handling

### 🎨 Frontend
- Responsive user interface
- Custom CSS styling
- Dark themed design

---

## 🛠 Tech Stack

### Backend
- Python
- Django 5
- Django Authentication System

### Database
- PostgreSQL (Production)
- SQLite (Development)

### Storage
- Cloudinary

### Deployment
- Render
- Gunicorn
- WhiteNoise

### Version Control
- Git
- GitHub

---

## 🏗 Project Architecture

```text
User Browser
      |
      ↓
Render Server
      |
      ↓
Gunicorn
      |
      ↓
Django Application
      |
      ├── PostgreSQL Database
      |
      ├── Cloudinary Media Storage
      |
      └── WhiteNoise Static Files
```

---

## 📂 Project Structure

```text
E-Library-Django/

├── elibrary_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── elibrary_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── management/
│
├── static/
│   └── css/
│
├── requirements.txt
├── manage.py
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/atishaya2020-gif/E-Library-Django.git
```

Move into the folder:

```bash
cd E-Library-Django
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run server:

```bash
python manage.py runserver
```

---

## 🔐 Environment Variables

Create environment variables:

```env
DATABASE_URL=

CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=

ADMIN_USERNAME=
ADMIN_EMAIL=
ADMIN_PASSWORD=
```

---

## 📸 Screenshots

(Add screenshots here)

---

## 🚀 Deployment

The application is deployed using Render:

Production services:

- Web Service → Render
- Database → PostgreSQL
- Media Files → Cloudinary
- Static Files → WhiteNoise

---

## 📚 Learning Outcomes

Through this project I learned:

- Django MVC/MVT architecture
- Authentication system
- Database models and migrations
- File upload handling
- Static and media file management
- PostgreSQL integration
- Cloud deployment workflow
- Environment variables
- Debugging production errors

---

## 👨‍💻 Developer

Created by **Atishaya Jain**

GitHub: https://github.com/atishaya2020-gif

---

⭐ If you like this project, consider giving it a star!
---
