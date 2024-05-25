import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resturant_project.settings')
django.setup()

User = get_user_model()

username = os.getenv('admin')
email = os.getenv('admin123@gmail.com')
password = os.getenv('Admin-password')

if username and email and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)

