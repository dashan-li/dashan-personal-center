# Dashan — Personal Website

A personal website built with Django 6, featuring a professional experience timeline and a self-managed tech blog. Deployed on Vercel with a Neon PostgreSQL database.

**Live site:** https://dashan.vercel.app

---

## Features

- **Homepage** — career overview, experience timeline, education, skills and stats
- **Experience page** — detailed work history with timeline layout
- **Blog** — article list and detail views with Markdown rendering, categories and tags
- **Admin** — full content management via Django Admin (`/admin/`)
  - Create / edit / publish articles (draft → published workflow)
  - Manage categories and tags
  - Bilingual support (English & Chinese)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 6.0 |
| Database | Neon PostgreSQL (production) / SQLite (local) |
| Static files | WhiteNoise |
| Media uploads | Cloudinary |
| Deployment | Vercel (serverless) |
| Markdown | mistune 3 |

---

## Project Structure

```
personal_center/
├── apps/
│   ├── core/               # Homepage and experience page
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── experience_data.py  # Career timeline data
│   └── blog/               # Article management
│       ├── models.py       # Article, Category, Tag
│       ├── views.py
│       ├── urls.py
│       └── admin.py
├── personal_center/
│   ├── settings/
│   │   ├── base.py         # Shared settings
│   │   ├── dev.py          # Local development (SQLite)
│   │   └── prod.py         # Production (Neon PostgreSQL, Vercel)
│   ├── urls.py
│   └── wsgi.py             # Auto-selects dev/prod via DATABASE_URL
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
├── build_files.sh          # Vercel build script (collectstatic + migrate)
├── vercel.json             # Vercel routing config
└── requirements.txt
```

---

## Local Development

**Prerequisites:** Python 3.12+

```bash
# Clone the repo
git clone https://github.com/dashan-li/dashan-personal-center.git
cd dashan-personal-center

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create admin account
python manage.py createsuperuser

# Start dev server
python manage.py runserver
```

Visit http://localhost:8000 — the site automatically uses SQLite in local mode.

Admin: http://localhost:8000/admin/

---

## Deployment (Vercel + Neon)

### 1. Create a Neon database

Sign up at [neon.tech](https://neon.tech) and copy the connection string:
```
postgresql://user:password@ep-xxx.neon.tech/neondb?sslmode=require
```

### 2. Set Vercel environment variables

In your Vercel project settings, add:

| Variable | Value |
|---|---|
| `DATABASE_URL` | Neon connection string |
| `SECRET_KEY` | A long random string |
| `ALLOWED_HOSTS` | `dashan.vercel.app` |
| `DJANGO_SETTINGS_MODULE` | `personal_center.settings.prod` |

Generate a secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 3. Run migrations and create superuser

Point your local environment at the Neon database and run:

```bash
DATABASE_URL="<your-neon-connection-string>" python manage.py migrate --settings=personal_center.settings.prod
DATABASE_URL="<your-neon-connection-string>" python manage.py createsuperuser --settings=personal_center.settings.prod
```

### 4. Deploy

```bash
vercel deploy --prod
```

---

## Writing Articles

1. Go to https://dashan.vercel.app/admin/
2. Log in with your superuser account
3. Navigate to **Blog → Articles → Add Article**
4. Write content in **Markdown** (English and/or Chinese)
5. Set status to **Published** when ready

---

## Environment Variables Reference

| Variable | Required | Description |
|---|---|---|
| `DATABASE_URL` | Production | Neon PostgreSQL connection string |
| `SECRET_KEY` | Production | Django secret key |
| `ALLOWED_HOSTS` | Production | Comma-separated list of allowed hostnames |
| `CLOUDINARY_CLOUD_NAME` | Optional | Cloudinary cloud name for image uploads |
| `CLOUDINARY_API_KEY` | Optional | Cloudinary API key |
| `CLOUDINARY_API_SECRET` | Optional | Cloudinary API secret |
