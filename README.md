# DevConnect API

Django REST Framework based API for developers with:

- JWT authentication (`/api/token/`, `/api/token/refresh/`)
- Profiles and posts
- Search on users/profiles/posts
- Pagination (`PageNumberPagination`)
- Global + scoped throttling
- Author-only post update/delete permissions

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Main Endpoints

- `POST /api/token/`
- `POST /api/token/refresh/`
- `GET /api/users/?search=<username-or-skill>`
- `GET /api/profiles/?search=<username-or-skill>`
- `GET /api/posts/?search=<title-or-content>&page=2`
- `POST /api/posts/create/` (JWT, scope throttle: `3/minute`)

## ModHeader test flow

1. Get token from `POST /api/token/`.
2. In ModHeader set:
   - `Authorization: Bearer <ACCESS_TOKEN>`
3. Call protected endpoints such as:
   - `POST /api/posts/create/`
   - `POST /api/profiles/`

If the header is missing/invalid, protected endpoints return 401.

## Throttling policy

- Anonymous: `5/minute`
- Authenticated: `20/minute`
- Scoped `posts_create`: `3/minute`
- Scoped `token`: `5/minute`

## Permissions

- Anyone can read posts.
- Only authenticated users can create posts/profiles.
- Only post author can update/delete own post.
