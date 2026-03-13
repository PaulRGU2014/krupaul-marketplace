# Learn the Project

This project is a simple full-stack starter made of three parts:

1. **Frontend** — Next.js app running on port `3000`
2. **Backend** — FastAPI app running on port `8000`
3. **Database** — PostgreSQL running on port `5432`

Right now, it is a clean scaffold for learning:
- the frontend shows a basic homepage
- the backend exposes a simple health endpoint
- the database is connected and ready
- the project structure is prepared for real features

## How the System Works

A normal request flow looks like this:

1. A user opens the frontend in the browser
2. Next.js renders the page
3. The frontend sends a request to the backend API
4. FastAPI receives the request
5. A route calls business logic in `services/`
6. The backend reads or writes data in PostgreSQL through SQLAlchemy
7. The backend returns JSON
8. The frontend displays the result

Docker ties these services together through [docker-compose.yml](docker-compose.yml).

## Backend Structure

### App startup
See [backend/app/main.py](backend/app/main.py).

This file:
- creates the FastAPI app
- enables CORS so the frontend can call the backend
- registers API routers
- defines the `/health` endpoint

This is the main backend entry point.

### Settings
See [backend/app/core/config.py](backend/app/core/config.py).

This file uses `BaseSettings` from `pydantic-settings`.

It stores configuration such as:
- `PROJECT_NAME`
- `API_V1_STR`
- `DATABASE_URL`
- `ALLOWED_ORIGINS`
- `SECRET_KEY`

This is a good place to learn:
- Python classes
- type hints
- environment variables
- config management

### Database session
See [backend/app/db/session.py](backend/app/db/session.py).

This file:
- creates the SQLAlchemy engine
- creates `SessionLocal`
- defines `Base` for all database models
- defines `get_db()` to open and close DB sessions safely

This is the core database connection layer.

### API router
See [backend/app/api/router.py](backend/app/api/router.py).

This file is where feature routers are connected.

Later, it can include routes like:
- `users`
- `products`
- `orders`

Think of it as the backend URL map.

### Models, schemas, and services
Folders:
- [backend/app/models](backend/app/models)
- [backend/app/schemas](backend/app/schemas)
- [backend/app/services](backend/app/services)

Each folder has a different purpose:

- **models**: database table definitions with SQLAlchemy
- **schemas**: request and response validation with Pydantic
- **services**: business logic

A useful mental model:
- model = how data is stored
- schema = how data enters and leaves the API
- service = what the application does

## Python Libraries in This Project

From [backend/requirements.txt](backend/requirements.txt):

- `fastapi` — web API framework
- `uvicorn` — server for running FastAPI
- `sqlalchemy` — ORM and database toolkit
- `alembic` — database migrations
- `psycopg2-binary` — PostgreSQL driver
- `pydantic` — validation and serialization
- `pydantic-settings` — config from environment variables
- `python-jose` — JWT token support
- `passlib` — password hashing
- `python-multipart` — form/file upload parsing
- `httpx` — making HTTP requests from Python

## Best Way to Learn Python Through This Project

### Phase 1: Learn plain Python
Focus on:
- variables
- functions
- classes
- imports
- lists and dictionaries
- type hints
- exceptions

### Phase 2: Learn FastAPI
Focus on:
- route functions
- path parameters
- query parameters
- request bodies
- response models
- dependencies

### Phase 3: Learn SQLAlchemy
Focus on:
- model classes
- columns and types
- sessions
- queries
- relationships

### Phase 4: Learn app architecture
Focus on:
- thin route handlers
- business logic in `services/`
- validation in `schemas/`
- persistence in `models/`

## Best Way to Study This Repo

A strong learning path is to build one feature end to end.

Example: a `Product` feature.

That would involve:
- `models/product.py`
- `schemas/product.py`
- `services/product_service.py`
- `api/endpoints/products.py`
- registering that router in [backend/app/api/router.py](backend/app/api/router.py)

That single feature teaches:
- Python classes
- FastAPI routes
- Pydantic schemas
- SQLAlchemy models
- database sessions
- separation of concerns

## Good Beginner Exercises

1. Add a route:
   - `GET /api/v1/hello`
   - return `{"message": "hello"}`

2. Add a `Product` schema with mock data
   - no database yet
   - just return a hardcoded product list

3. Add a real `Product` model
   - fields like `id`, `name`, `price`

4. Add API routes:
   - `POST /products`
   - `GET /products`

5. Add an Alembic migration for the `Product` table

## Important Truth About the Current Project

This is not yet a complete marketplace.

It is a well-structured starter project that is ideal for learning.

Current state:
- frontend is minimal
- backend is minimal
- database is ready
- project structure is ready for features

That is a good place to start learning because the codebase is not overloaded yet.

## A Simple Mental Model

Use this when navigating the backend:

- `main.py` = start the app
- `router.py` = connect routes
- `schemas/` = validate data
- `models/` = store data
- `services/` = business logic
- `db/session.py` = database connection handling
- `.env` = configuration

## Suggested Next Step

The best next lesson is to build a `Product` feature from scratch.

That would teach nearly all the important Python backend concepts in this repo.
