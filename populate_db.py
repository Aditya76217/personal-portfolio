import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from portfolio.models import Profile, Skill, Education, Certification, Achievement
from projects.models import Project


def populate():
    # Clear existing data
    Profile.objects.all().delete()
    Skill.objects.all().delete()
    Education.objects.all().delete()
    Certification.objects.all().delete()
    Achievement.objects.all().delete()
    Project.objects.all().delete()

    # ── Profile ──────────────────────────────────────────
    Profile.objects.create(
        name="Aditya Malviya",
        titles="Software Engineer • App Developer • Cyber Security Engineer • Web Developer",
        tagline="Full Stack Developer | AI Enthusiast | Cyber Security Geek",
        location="Prayagraj, Uttar Pradesh, India",
        address="35/7K/1 Jayantipur, Dhoomanganj, Prayagraj",
        phone="+91 9335145900",
        email="adityamalviya217@gmail.com",
        linkedin="https://www.linkedin.com/in/aditya-malviya-314a57202",
        github="https://github.com/Aditya76217",
        summary="Aspiring Software Engineer and a B.Tech CSE student at IIMT College of Engineering. "
                "I am passionate about Web/App Development and Cyber Security, constantly exploring new technologies. "
                "As an avid chess player, I bring a strategic and problem-solving mindset to my work.",
        career_vision="My vision is to become a versatile Full-Stack Developer and Cyber Security expert, "
                      "building secure and intelligent web applications that make a real-world impact. "
                      "I aim to contribute to open-source projects and eventually lead an innovative tech startup."
    )

    # ── Skills ───────────────────────────────────────────
    skills_data = [
        # Frontend
        ("HTML5", "Frontend", "Advanced", 90, "fa-brands fa-html5"),
        ("CSS3", "Frontend", "Advanced", 85, "fa-brands fa-css3-alt"),
        ("JavaScript", "Frontend", "Intermediate", 75, "fa-brands fa-js"),
        # Backend
        ("Python", "Backend", "Advanced", 88, "fa-brands fa-python"),
        ("Django", "Backend", "Intermediate", 78, "fa-solid fa-server"),
        ("Java", "Backend", "Advanced", 85, "fa-brands fa-java"),
        ("C#", "Backend", "Intermediate", 70, "fa-solid fa-code"),
        # Database
        ("SQLite", "Database", "Intermediate", 75, "fa-solid fa-database"),
        ("MySQL", "Database", "Intermediate", 70, "fa-solid fa-database"),
        ("MongoDB", "Database", "Beginner", 50, "fa-solid fa-leaf"),
        # Tools
        ("GitHub", "Tools", "Advanced", 85, "fa-brands fa-git-alt"),
        ("VS Code", "Tools", "Advanced", 90, "fa-solid fa-laptop-code"),
        ("Linux", "Tools", "Intermediate", 72, "fa-brands fa-linux"),
        # Top Skills (for sidebar / chatbot)
        ("Java", "Top Skills", "", 85, "fa-brands fa-java"),
        ("C#", "Top Skills", "", 70, "fa-solid fa-code"),
        ("Python", "Top Skills", "", 90, "fa-solid fa-brain"),
        # Languages
        ("Hindi", "Languages", "Native or Bilingual", 100, ""),
        ("English", "Languages", "Professional Working", 80, ""),
    ]

    for name, category, proficiency, percent, icon in skills_data:
        Skill.objects.create(
            name=name,
            category=category,
            proficiency=proficiency,
            proficiency_percent=percent,
            icon_class=icon,
        )

    # ── Education ────────────────────────────────────────
    Education.objects.create(
        institution="IIMT College of Engineering, Greater Noida",
        degree="Bachelor of Technology — Computer Science & Engineering",
        date_range="2024 – 2028",
        description="Studied core CS subjects including Data Structures, Algorithms, "
                    "Operating Systems, Databases, Computer Networks, and Cyber Security."
    )

    # ── Certifications ───────────────────────────────────
    certs = [
        ("Introduction to Programming Using Python", "Hackerrank", "2025"),
        ("Certified Ethical Hacker (CEH)", "Craw Security", "2024"),
        ("Data Analysis with Python", "Coursera", "2025"),
        ("Ignite 2k25", "Tech Fest", "2025"),
        ("Google AI Professional Certificate", "Google", "2026"),

    ]
    for title, issuer, date in certs:
        Certification.objects.create(title=title, issuer=issuer, date=date)

    # ── Achievements ─────────────────────────────────────
    achievements = [
        ("Ignite 2k25", "Taken Part in the event", "2025", "fa-solid fa-trophy"),
        ("Certified Ethical Hacker", "Earned the globally recognized CEH certification from EC-Council", "2024", "fa-solid fa-shield-halved"),
        ("Open Source Contributor", "Contributed to multiple open-source Python and Django projects", "2025", "fa-brands fa-github"),
        ("Google AI Professional Certificate", "Completed the Google AI Professional Certificate program", "2026", "fa-solid fa-chess-knight"),
    ]
    for title, desc, date, icon in achievements:
        Achievement.objects.create(title=title, description=desc, date=date, icon_class=icon)

    # ── Projects ─────────────────────────────────────────
    projects_data = [
    (
        "Personal Portfolio Website",
        "A dynamic, full-stack portfolio website with glassmorphism UI, Django backend, "
        "and an AI-powered chatbot with offline rule-based fallback.",
        "Django, Python, HTML/CSS/JS, SQLite, OpenAI",
        "https://github.com/Aditya76217/personal-portfolio"
    ),
    (
        "Student Grade Calculator",
        "A structured Java console application that calculates student grades using OOP principles. "
        "Includes classes like Student, Subject, and Result, with input validation and exception handling. "
        "Implements interfaces and method overriding to support multiple grading schemes.",
        "Java, OOP, Exception Handling",
        "https://github.com/Aditya76217/student-grade-calculator"
    ),
    (
        "Library Management System",
        "A menu-driven Python application to manage library operations such as adding, searching, issuing, "
        "and returning books. Uses classes like Book, Member, and Library with file handling for data persistence "
        "and handles real-world edge cases effectively.",
        "Python, File Handling, OOP",
        "https://github.com/Aditya76217/library-management-system"
    ),
    (
        "Task Manager Pro",
        "A feature-rich task management web application with a drag-and-drop Kanban board, priority levels, "
        "due date tracking, and team collaboration features for efficient workflow management.",
        "Django, JavaScript, SQLite, Bootstrap",
        "https://github.com/Aditya76217/task-manager-pro"
    )
]

    for title, desc, stack, link in projects_data:
        Project.objects.create(
            title=title,
            description=desc,
            tech_stack=stack,
            github_link=link,
        )

    print("Database populated successfully!")


if __name__ == '__main__':
    populate()
