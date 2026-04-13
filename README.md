# 🚀 Aditya Malviya — Developer Portfolio

<div align="center">

![Django](https://img.shields.io/badge/Django-4.2.7-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

**A full-stack developer portfolio with an integrated AI chatbot, dynamic project showcase, and contact system — built with Django.**

[Live Demo](https://aditya76-portfolio.vercel.app) · [Report Bug](https://github.com/Aditya76217/portfolio_project/issues) · [Request Feature](https://github.com/Aditya76217/portfolio_project/issues)

</div>

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Apps Overview](#-apps-overview)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🧑‍💻 About the Project

This is a personal developer portfolio for **Aditya Malviya**, a B.Tech Computer Science student from IIMT College of Engineering, Greater Noida. The portfolio is a full-stack Django web application that showcases skills, projects, education, certifications, and achievements — all managed via Django's admin panel and a database backend.

The standout feature is the **integrated AI Chatbot**, which works offline using a rule-based engine and upgrades to OpenAI GPT-3.5 when an API key is available.

---

## ✨ Features

- 🎨 **Dynamic Portfolio Page** — Profile, skills, education, certifications, and achievements rendered from the database
- 🤖 **AI Chatbot** — Offline-first rule-based assistant with optional OpenAI GPT-3.5 fallback
- 🚀 **Projects Showcase** — Projects with title, description, tech stack, and GitHub links
- 📧 **Contact Form** — Users can submit messages stored directly in the database
- 🛠️ **Django Admin Panel** — Full CRUD for all portfolio content (no hardcoding needed)
- 📱 **Responsive Design** — Mobile-friendly frontend with custom CSS and JavaScript
- ⚡ **Vercel Deployment** — Configured and live on Vercel

---

## 📁 Project Structure

```
portfolio_project/
│
├── portfolio_site/          # Django project settings & root URLs
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── portfolio/               # Main portfolio app
│   ├── models.py            # Profile, Skill, Education, Certification, Achievement
│   ├── views.py             # Home view — renders full portfolio page
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│   │   └── portfolio/
│   │       └── index.html   # Single-page portfolio template
│   └── static/
│       └── portfolio/
│           ├── css/         # style.css, chatbot.css
│           └── js/          # script.js, chatbot.js
│
├── projects/                # Projects app
│   ├── models.py            # Project model (title, description, tech_stack, github_link)
│   ├── views.py
│   └── urls.py
│
├── contact/                 # Contact form app
│   ├── models.py            # Contact model (name, email, message, timestamp)
│   ├── views.py
│   └── urls.py
│
├── chatbot/                 # AI Chatbot app
│   ├── models.py            # ChatMessage model (user_message, bot_response)
│   ├── views.py             # Rule-based + OpenAI API logic
│   └── urls.py
│
├── populate_db.py           # Script to seed the database with initial data
├── manage.py
├── requirements.txt
├── .env                     # Environment variables (not committed)
└── db.sqlite3
```

---

## 🛠️ Tech Stack

| Layer        | Technology                          |
|--------------|-------------------------------------|
| Backend      | Python, Django 4.2.7                |
| Frontend     | HTML5, CSS3, JavaScript             |
| Database     | SQLite (development)                |
| AI / Chatbot | Rule-based engine + OpenAI GPT-3.5  |
| Deployment   | Vercel                              |
| Styling      | Custom CSS (no framework)           |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Aditya76217/portfolio_project.git
   cd portfolio_project
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   pip install python-dotenv openai   # For chatbot AI features
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Seed the database** *(optional but recommended)*

   ```bash
   python populate_db.py
   ```

6. **Create a superuser** *(for admin panel access)*

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` in your browser.

---

### Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY="your-openai-api-key-here"
```

> **Note:** The chatbot works without an API key using offline rule-based responses. OpenAI is used as an optional fallback for unrecognized queries.

> ⚠️ **Security Warning:** Never commit your `.env` file or expose your secret key. Make sure `.env` is listed in `.gitignore`. Also replace the `SECRET_KEY` in `settings.py` before deploying to production.

---

## 💡 Usage

- Visit the homepage to view the full portfolio
- Click the **💬 Chat** button to interact with the AI assistant
- Fill out the **Contact Form** to send a message
- Visit `/admin` to manage all content via Django Admin
- The chatbot understands queries about: `skills`, `projects`, `contact`, `resume`, `education`, `experience`, `about`, `location`

---

## 🔌 API Endpoints

| Method | Endpoint            | Description                      |
|--------|---------------------|----------------------------------|
| GET    | `/`                 | Main portfolio page              |
| POST   | `/api/chat/`        | Chatbot API — send a message     |
| POST   | `/api/contact/`     | Submit contact form              |
| GET    | `/api/projects/`    | List all projects                |
| GET    | `/admin/`           | Django admin panel               |

**Chatbot API Example:**

```bash
curl -X POST http://127.0.0.1:8000/api/chat/ \
  -H "Content-Type: application/json" \
  -d '{"message": "What are your skills?"}'
```

```json
{
  "bot_response": "💻 Aditya's Technical Skills: ..."
}
```

---

## 📦 Apps Overview

### `portfolio`
The core app. Renders the single-page portfolio with all data pulled from:
- `Profile` — Name, tagline, social links, summary
- `Skill` — Categorized skills (Frontend, Backend, Database, Tools, Languages, Top Skills) with proficiency percentages
- `Education` — Degrees and institutions
- `Certification` — Certificates and issuers
- `Achievement` — Awards and accomplishments

### `projects`
Manages the projects showcase. Each `Project` has a title, description, tech stack, and an optional GitHub link.

### `contact`
Handles the contact form. Submitted `Contact` entries (name, email, message) are stored with a timestamp.

### `chatbot`
Two-tier AI chatbot:
1. **Rule-based (offline)** — Handles greetings, skills, projects, contact, resume, education, achievements, about, and help queries
2. **OpenAI GPT-3.5 (online)** — Activated when `OPENAI_API_KEY` is set; used for unrecognized queries
3. **Graceful fallback** — If OpenAI is unavailable, suggests available topics

All chat history is saved in the `ChatMessage` model.

---

## ☁️ Deployment

This project is deployed on **Vercel**. The `ALLOWED_HOSTS` in `settings.py` includes `aditya76-portfolio.vercel.app`.

For production deployment:
- Set `DEBUG = False`
- Use a strong, secret `SECRET_KEY` (store in environment variables)
- Run `python manage.py collectstatic`
- Configure a production database (e.g., PostgreSQL)

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📬 Contact

**Aditya Malviya**

- 📧 Email: [adityamalviya217@gmail.com](mailto:adityamalviya217@gmail.com)
- 💼 LinkedIn: [aditya-malviya-314a57202](https://www.linkedin.com/in/aditya-malviya-314a57202)
- 🐙 GitHub: [@Aditya76217](https://github.com/Aditya76217)

---

<div align="center">
  Made with ❤️ by <a href="https://github.com/Aditya76217">Aditya Malviya</a>
</div>
