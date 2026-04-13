from django.shortcuts import render
from .models import Profile, Skill, Education, Certification, Achievement
from projects.models import Project


def home(request):
    """Render the main portfolio page with all context data."""
    profile = Profile.objects.first()

    # Skills grouped by category
    frontend_skills = Skill.objects.filter(category='Frontend')
    backend_skills = Skill.objects.filter(category='Backend')
    database_skills = Skill.objects.filter(category='Database')
    tools_skills = Skill.objects.filter(category='Tools')
    languages = Skill.objects.filter(category='Languages')
    top_skills = Skill.objects.filter(category='Top Skills')

    all_skills = Skill.objects.all()
    education = Education.objects.all()
    certifications = Certification.objects.all()
    achievements = Achievement.objects.all()
    projects = Project.objects.all()

    context = {
        'profile': profile,
        'all_skills': all_skills,
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'database_skills': database_skills,
        'tools_skills': tools_skills,
        'languages': languages,
        'top_skills': top_skills,
        'education': education,
        'certifications': certifications,
        'achievements': achievements,
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', context)
