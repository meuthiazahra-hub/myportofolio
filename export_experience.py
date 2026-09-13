import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "namaproject.settings")
django.setup()

from main.models import Experience

html = ""
for e in Experience.objects.all():
    status = "Sedang berlangsung" if e.is_ongoing else "Selesai"
    html += f"""
            <article class="experience-card">
                <span class="experience-category">{e.get_category_display()}</span>
                <h2>{e.title}</h2>
                <p class="experience-description">{e.description}</p>
                <p class="experience-status">{status}</p>
            </article>
"""

print(html)