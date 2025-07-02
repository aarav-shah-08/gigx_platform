# GigX Platform 🎯

A Django-based gig management system for Providers and Seekers.

## 🔧 Features
- Role-based dashboards
- Providers: Post and view gigs
- Seekers: View, favorite, and apply for gigs
- Favorite functionality using ManyToManyField
- Environment variables using `.env`

## 🧪 Setup Instructions
```bash
git clone https://github.com/yourusername/gigx_platform.git
cd gigx_platform
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
