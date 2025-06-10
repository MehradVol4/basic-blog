# 📝 Basic Blog

A fully functional blog web application built with **Django**, featuring user registration, authentication, profile management, and full CRUD operations for blog posts.

## 🚀 Features

- User Registration, Login, Logout
- Profile Picture Upload
- Create, Read, Update, Delete (CRUD) for Posts
- Post detail and list views
- About Page
- Customizable styling via `main.css`
- Media handling for user-uploaded images

## 🛠️ Tech Stack

- **Backend**: Python 3.12, Django
- **Database**: SQLite (default)
- **Frontend**: HTML, CSS (custom styling via `main.css`)
- **Media**: Django Media files (e.g., profile pictures)

## 📁 Project Structure

```
basic-blog/
├── blog/              # Django project settings
├── blog_app/          # Main app handling blog posts
├── users_app/         # Handles user registration, login, profiles
├── media/             # Uploaded media files
├── db.sqlite3         # SQLite DB
├── manage.py          # Django's management script
```

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MehradVol4/basic-blog.git
cd basic-blog
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the app in your browser.

## 🖼️ Media Handling

- Uploaded profile pictures are stored in `/media/profile_pics/`
- Default image fallback is available as `default.jpg`

Make sure to enable media file serving in `settings.py` during development:

```python
# At the bottom of settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# In urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 📄 Templates Overview

- `blog_app/templates/blog_app/`
  - `home.html`, `post-create.html`, `post-details.html`, etc.
- `users_app/templates/users_app/`
  - `login.html`, `register.html`, `profile.html`, etc.
- `base.html`: Main layout with navbar/footer

## 🧪 Running Tests

```bash
python manage.py test
```

(Tests located in `tests.py` in each app.)

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/foo`)
3. Commit your changes (`git commit -am 'Add foo'`)
4. Push to the branch (`git push origin feature/foo`)
5. Create a new Pull Request

