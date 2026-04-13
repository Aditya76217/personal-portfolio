"""
Chatbot API View
================
Priority flow:
1. Check rule-based responses (works OFFLINE)
2. If no match → call OpenAI API (needs internet)
3. Fallback → helpful error message
"""
import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage
from projects.models import Project

# ── Try to import OpenAI ────────────────────────────────
try:
    import openai
    from dotenv import load_dotenv
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    OPENAI_AVAILABLE = bool(openai.api_key and openai.api_key != "your-openai-api-key-here")
except ImportError:
    OPENAI_AVAILABLE = False


# ── Rule-Based Responses (OFFLINE-FIRST) ────────────────
def get_rule_response(message):
    """
    Check the user message against predefined rules.
    Returns a response string if matched, or None.
    """
    msg = message.lower().strip()

    # Greetings
    greetings = ["hi", "hello", "hey", "hola", "greetings", "sup", "yo", "good morning", "good evening"]
    if msg in greetings or any(msg.startswith(g) for g in ["hi ", "hello ", "hey "]):
        return (
            "👋 Hello! I'm <strong>Aditya's AI Assistant</strong>. "
            "I can help you with:\n\n"
            "• 💻 <strong>Skills</strong> & technologies\n"
            "• 🚀 <strong>Projects</strong> I've built\n"
            "• 📧 <strong>Contact</strong> information\n"
            "• 📄 <strong>Resume</strong> download\n"
            "• 🎓 <strong>Education</strong> & experience\n\n"
            "What would you like to know?"
        )

    # Skills
    if any(kw in msg for kw in ["skill", "skills", "technologies", "tech stack", "what do you know", "what can you do"]):
        return (
            "💻 <strong>Aditya's Technical Skills:</strong>\n\n"
            "🎨 <strong>Frontend:</strong> HTML5, CSS3, JavaScript, React\n"
            "⚙️ <strong>Backend:</strong> Python, Django, Java, C#\n"
            "🗄️ <strong>Database:</strong> SQLite, MySQL, MongoDB\n"
            "🛠️ <strong>Tools:</strong> Git & GitHub, VS Code, Linux, Docker\n"
            "🧠 <strong>Other:</strong> AI/ML, Cyber Security, Data Analysis"
        )

    # Projects — Fetch from database
    if any(kw in msg for kw in ["project", "projects", "portfolio", "work", "built", "show projects"]):
        try:
            projects = Project.objects.all()
            if projects.exists():
                proj_list = "\n".join(
                    [f"• <strong>{p.title}</strong> — {p.tech_stack}" for p in projects]
                )
                return f"🚀 <strong>Aditya's Projects:</strong>\n\n{proj_list}\n\nScroll down to the Projects section for more details!"
            else:
                return "🚀 I'm currently working on exciting projects! Check back soon or scroll to the Projects section."
        except Exception:
            return "🚀 Check out the Projects section below to see all of Aditya's work!"

    # Contact
    if any(kw in msg for kw in ["contact", "email", "hire", "reach", "phone", "call", "connect"]):
        return (
            "📧 <strong>Contact Information:</strong>\n\n"
            "• ✉️ Email: <strong>adityamalviya217@gmail.com</strong>\n"
            "• 📱 Phone: <strong>09335145900</strong>\n"
            "• 💼 LinkedIn: <a href='https://www.linkedin.com/in/aditya-malviya-314a57202' target='_blank'>View Profile</a>\n"
            "• 🐙 GitHub: <a href='https://github.com/Aditya76217' target='_blank'>View Repos</a>\n\n"
            "Or fill out the <strong>Contact Form</strong> below! 👇"
        )

    # Resume
    if any(kw in msg for kw in ["resume", "cv", "download resume", "curriculum"]):
        return (
            "📄 You can download Aditya's resume by clicking the "
            "<strong>Download Resume</strong> button at the bottom of the page. "
            "It includes all skills, experience, and projects! 📥"
        )

    # Education
    if any(kw in msg for kw in ["education", "college", "university", "degree", "study", "school", "b.tech", "btech"]):
        return (
            "🎓 <strong>Education:</strong>\n\n"
            "• <strong>B.Tech — Computer Science & Engineering</strong>\n"
            "• IIMT College of Engineering, Greater Noida\n"
            "• Graduation: 2024\n\n"
            "Core subjects: Data Structures, Algorithms, OS, Databases, "
            "Computer Networks, and Cyber Security."
        )

    # Experience / Achievements
    if any(kw in msg for kw in ["experience", "achievement", "hackathon", "certification", "cert", "award"]):
        return (
            "🏆 <strong>Key Achievements:</strong>\n\n"
            "• 🏅 Hackathon Finalist — Ignite 2k25 (500+ teams)\n"
            "• 🛡️ Certified Ethical Hacker (CEH) — EC-Council\n"
            "• 🐙 Open Source Contributor — Python & Django projects\n"
            "• ♟️ Chess Tournament Winner — Inter-college\n\n"
            "📜 <strong>Certifications:</strong> SEE THE WORLD THROUGH AI, "
            "Python Programming, Data Analysis with Python"
        )

    # About
    if any(kw in msg for kw in ["about", "who", "tell me about", "introduce"]):
        return (
            "👨‍💻 <strong>About Aditya Malviya:</strong>\n\n"
            "Aspiring Software Engineer and B.Tech CSE student at IIMT College of Engineering. "
            "Passionate about Web/App Development and Cyber Security. "
            "An avid chess player with a strategic problem-solving mindset.\n\n"
            "🎯 <strong>Vision:</strong> To become a versatile Full-Stack Developer and "
            "Cyber Security expert, building secure and intelligent web applications."
        )

    # Location
    if any(kw in msg for kw in ["location", "where", "city", "place", "address"]):
        return (
            "📍 <strong>Location:</strong>\n\n"
            "Prayagraj, Uttar Pradesh, India 🇮🇳\n\n"
            "Open to remote opportunities and relocation! 🌍"
        )

    # Thank you
    if any(kw in msg for kw in ["thank", "thanks", "thx", "appreciate"]):
        return "😊 You're welcome! Feel free to ask anything else or use the contact form to get in touch. Have a great day! 👋"

    # Goodbye
    if any(kw in msg for kw in ["bye", "goodbye", "see you", "later", "cya"]):
        return "👋 Goodbye! Thanks for visiting Aditya's portfolio. Don't forget to check out the projects and feel free to connect! 🚀"

    # Help
    if any(kw in msg for kw in ["help", "what can you", "options", "menu"]):
        return (
            "🤖 <strong>I can help you with:</strong>\n\n"
            "• 💬 Say <strong>'skills'</strong> — See technical skills\n"
            "• 💬 Say <strong>'projects'</strong> — View all projects\n"
            "• 💬 Say <strong>'contact'</strong> — Get contact info\n"
            "• 💬 Say <strong>'resume'</strong> — Download resume\n"
            "• 💬 Say <strong>'education'</strong> — Education details\n"
            "• 💬 Say <strong>'experience'</strong> — Achievements & certs\n"
            "• 💬 Say <strong>'about'</strong> — Learn about Aditya\n\n"
            "Or just ask me anything! 😄"
        )

    # No match
    return None


@csrf_exempt
def chat_api(request):
    """
    Chatbot API endpoint.
    POST /api/chat/ with JSON body: { "message": "user text" }
    Returns: { "bot_response": "..." }
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method.'}, status=405)

    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()

        if not user_message:
            return JsonResponse({'bot_response': 'Please type a message! 😊'}, status=400)

        # ── STEP 1: Rule-based response (OFFLINE) ──
        rule_response = get_rule_response(user_message)
        if rule_response:
            # Save to history
            ChatMessage.objects.create(
                user_message=user_message,
                bot_response=rule_response
            )
            return JsonResponse({'bot_response': rule_response})

        # ── STEP 2: OpenAI API fallback (ONLINE) ──
        if OPENAI_AVAILABLE:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an AI assistant for Aditya Malviya's developer portfolio. "
                                "Aditya is a B.Tech CSE student at IIMT College of Engineering who specializes in "
                                "Python, Django, Java, C#, Web Development, AI, and Cyber Security. "
                                "Answer questions about skills, projects, and experience. "
                                "Be professional, concise, and helpful. Keep answers brief."
                            )
                        },
                        {"role": "user", "content": user_message}
                    ],
                    max_tokens=200,
                    temperature=0.7,
                )
                bot_response = response.choices[0].message['content'].strip()
            except Exception:
                bot_response = (
                    "🤔 I couldn't reach my AI brain right now, but I can still help! "
                    "Try asking about <strong>skills</strong>, <strong>projects</strong>, "
                    "<strong>contact</strong>, or <strong>education</strong>!"
                )
        else:
            # ── STEP 3: Graceful fallback ──
            bot_response = (
                "🤔 I'm not sure about that, but I can help with:\n\n"
                "• <strong>Skills</strong> — My technical abilities\n"
                "• <strong>Projects</strong> — What I've built\n"
                "• <strong>Contact</strong> — How to reach me\n"
                "• <strong>Resume</strong> — Download my CV\n"
                "• <strong>Education</strong> — My background\n\n"
                "Try one of these topics! 😊"
            )

        # Save to history
        ChatMessage.objects.create(
            user_message=user_message,
            bot_response=bot_response
        )

        return JsonResponse({'bot_response': bot_response})

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
