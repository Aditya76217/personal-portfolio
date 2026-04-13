from django.http import JsonResponse
from .models import Project

def get_projects(request):
    projects = Project.objects.all().values('title', 'description', 'tech_stack', 'github_link')
    return JsonResponse(list(projects), safe=False)
