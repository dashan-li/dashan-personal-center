#!/bin/bash
set -e

# Install dependencies — use --break-system-packages for PEP 668 / uv-managed envs
pip install --break-system-packages -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput --settings=personal_center.settings.prod

# Run migrations only if DATABASE_URL is available
if [ -n "$DATABASE_URL" ]; then
  python manage.py migrate --settings=personal_center.settings.prod
else
  echo "DATABASE_URL not set — skipping migrate"
fi
