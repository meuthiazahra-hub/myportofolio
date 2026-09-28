import uuid
from django.conf import settings
from django.db import models


class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ("internship", "Internship"),
        ("research", "Research"),
        ("volunteer", "Volunteer"),
        ("part-time", "Part-Time"),
        ("full-time", "Full-Time"),
        ("freelance", "Freelance"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default="full-time",
    )
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="starred_projects",
        blank=True,
    )

    def __str__(self):
        return self.title

class Achievement(models.Model):
    LEVEL_CHOICES = [
        ('campus', 'Campus'),
        ('national', 'National'),
        ('international', 'International'),
    ]
    title = models.CharField(max_length = 200)
    description = models.TextField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='campus')
    achieved_at = models.DateField()
    @property
    def is_top_tier(self):
        return self.level in ['national', 'international']


    
