# Krupaul Marketplace

A full-stack marketplace application built with **Next.js** (frontend) and **FastAPI** (backend), backed by **PostgreSQL**.

## Docker Prerequisites

- Run Docker commands from the project root: [docker-compose.yml](docker-compose.yml)
- Make sure [backend/.env.example](backend/.env.example) has been copied to [backend/.env](backend/.env)
- Your user must have permission to access the Docker daemon

### If Docker was installed with Snap

This machine is using Snap Docker, which commonly causes `permission denied` errors on `/var/run/docker.sock`.

Quick workaround:

```bash
sudo docker compose up --build
```

Preferred fix on Ubuntu:

```bash
sudo snap remove docker

# install Docker Engine from Docker's official apt repo
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
	"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
	$(. /etc/os-release && echo $VERSION_CODENAME) stable" | \
	sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo groupadd docker 2>/dev/null || true
sudo usermod -aG docker $USER
newgrp docker
docker --version
docker compose version
```

If `apt` reports `Could not get lock /var/lib/dpkg/lock-frontend` and mentions `unattended-upgr`, wait a minute or two for the background Ubuntu update to finish, then rerun the failed `apt-get install` command. Do not delete the lock file manually.

Then reopen the terminal and run:

```bash
docker compose up --build
```

## Stack

| Layer     | Technology              |
|-----------|-------------------------|
| Frontend  | Next.js 15, TypeScript  |
| Backend   | FastAPI, SQLAlchemy 2   |
| Database  | PostgreSQL 16           |
| Migrations| Alembic                 |
| Container | Docker / Docker Compose |

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── api/          # Route handlers
│   │   ├── core/         # Settings & config
│   │   ├── db/           # DB session & base model
│   │   ├── models/       # SQLAlchemy models
│   │   ├── schemas/      # Pydantic schemas
│   │   └── services/     # Business logic
│   ├── alembic/          # Database migrations
│   ├── alembic.ini
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app/              # Next.js App Router pages
│   ├── components/       # Reusable React components
│   ├── public/           # Static assets
│   ├── next.config.js
│   ├── package.json
│   └── Dockerfile
└── docker-compose.yml
```

## Getting Started

### With Docker (recommended)

```bash
cp backend/.env.example backend/.env
docker compose up --build
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs (Swagger): http://localhost:8000/docs

### Local Development

**Backend**

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend**

```bash
cd frontend
npm install
npm run dev
```

### Database Migrations

```bash
# Create a new migration
docker compose exec backend alembic revision --autogenerate -m "description"

# Apply migrations
docker compose exec backend alembic upgrade head
```

## Environment Variables

Copy `.env.example` to `.env` in the `backend/` directory and update values as needed.

| Variable                       | Default                                        | Description              |
|--------------------------------|------------------------------------------------|--------------------------|
| `DATABASE_URL`                 | `postgresql://user:password@db:5432/marketplace` | PostgreSQL connection URL |
| `SECRET_KEY`                   | `change-me-in-production`                      | JWT signing secret       |
| `ACCESS_TOKEN_EXPIRE_MINUTES`  | `1440`                                         | Token TTL in minutes     |
| `ALLOWED_ORIGINS`              | `["http://localhost:3000"]`                    | CORS allowed origins     |
