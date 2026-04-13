from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    titles = models.CharField(max_length=255, help_text="Comma or dot separated titles")
    tagline = models.CharField(max_length=255, blank=True, default="Full Stack Developer | AI Enthusiast")
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    linkedin = models.URLField()
    github = models.URLField(blank=True, default="https://github.com/Aditya76217")
    summary = models.TextField()
    career_vision = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Database', 'Database'),
        ('Tools', 'Tools'),
        ('Top Skills', 'Top Skills'),
        ('Languages', 'Languages'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    proficiency = models.CharField(max_length=100, blank=True, null=True)
    proficiency_percent = models.IntegerField(default=70, help_text="0-100 for progress bars")
    icon_class = models.CharField(max_length=100, blank=True, default="", help_text="Font Awesome class e.g. fa-brands fa-python")

    def __str__(self):
        return f"{self.name} ({self.category})"


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    date_range = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.degree


class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200, blank=True, default="")
    date = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.CharField(max_length=100, blank=True, default="")
    icon_class = models.CharField(max_length=100, blank=True, default="fa-solid fa-trophy")

    def __str__(self):
        return self.title
