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

## Marketplace Architecture Mindset

This is the backbone for how to think about the app before writing much code.

### 1. The big idea behind a marketplace

A marketplace connects two sides:

- **Sellers** — people who list items or services
- **Buyers** — people who browse and purchase

As the platform, the real responsibilities are:

- trust
- payments
- discovery
- communication
- transactions

Everything else is implementation detail around those core problems.

### 2. Core marketplace features (MVP)

These are the features that make a marketplace feel real without making the project too large too early.

#### User accounts
- sign up / login
- buyer vs seller roles
- profile settings

#### Listings
- create listing
- upload images
- set price, description, category
- edit/delete listing

#### Browsing
- search
- filters
- categories
- pagination

#### Checkout
- add to cart (optional)
- buy now
- Stripe payment
- order confirmation

#### Orders
- buyer sees order history
- seller sees sales
- status updates

#### Dashboards
- buyer dashboard
- seller dashboard
- admin dashboard

#### Admin tools
- approve listings
- remove bad content
- manage users

This is the basic foundation of a real marketplace.

### 3. The product-building workflow

This is the clean order to think through the system.

#### Step 1 — Define the data model
Start with the core tables or entities:

- users
- listings
- orders
- payments
- images
- categories

This defines the shape of the system.

#### Step 2 — Build the backend API
The backend becomes the brain of the marketplace.

Typical endpoints might include:

- `POST /auth/register`
- `POST /listings`
- `GET /listings`
- `POST /checkout`
- `GET /orders`

#### Step 3 — Build the frontend pages
Match backend capabilities with UI pages.

Examples:

- `/` → homepage
- `/listings` → browse page
- `/listing/[id]` → listing detail page
- `/dashboard` → seller dashboard
- `/auth/login` → login page

This is where the product becomes visible to the user.

#### Step 4 — Add payments
This is where the marketplace becomes monetizable.

- buyers pay
- sellers get payouts
- the platform can take a fee

#### Step 5 — Add admin tools
This is what makes the system safer and more maintainable.

- approve listings
- remove spam
- manage disputes

#### Step 6 — Polish the UX
Important details include:

- loading states
- error messages
- empty states
- responsive design

#### Step 7 — Deploy
Eventually the system gets hosted in separate places:

- backend
- frontend
- database

### 4. The architecture mental model

This is the mindset to keep while learning.

#### The backend is the source of truth
It handles:

- business logic
- validation
- security
- payments
- database access

#### The frontend is the experience
It handles:

- UI
- navigation
- forms
- API calls

#### The database is the memory
It stores:

- users
- listings
- orders
- payments

#### The workflow is the glue
It defines:

- how data flows
- how users interact
- how transactions happen

Once this model is clear, the system becomes much easier to reason about.

### 5. The developer workflow to follow

This is the repeatable order that keeps the project organized:

1. start with the database
2. build the backend endpoints
3. connect the frontend
4. add authentication
5. add payments
6. add dashboards
7. add admin tools
8. polish and deploy

This is a strong workflow because each step depends naturally on the one before it.

### 6. Important learning note for this project

The goal here is not to have the system built for you.

The goal is to use this project to learn:

- Python
- FastAPI
- SQLAlchemy
- API design
- marketplace architecture

That means the best approach is to understand the shape of the system first, then build one piece at a time yourself.

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

## Fast Learning Path (from Node.js/Next.js to Python/FastAPI)

Your JavaScript background is a major advantage. You are not starting from zero — you are mostly translating familiar backend ideas into Python syntax and FastAPI conventions.

### Concept mapping (what you already know)

- Express route handler → FastAPI path operation (`@app.get`, `@router.post`)
- Next.js API JSON responses → FastAPI automatic JSON responses
- TypeScript interfaces/types → Pydantic schemas
- Prisma/ORM models → SQLAlchemy models
- Middleware in Node → middleware/dependencies in FastAPI
- `.env` config in Node → `BaseSettings` in `pydantic-settings`
- Migration tools in JS stacks → Alembic migrations

### What to focus on first (Python-specific)

1. **Python syntax differences**
   - indentation instead of braces
   - type hints (`str`, `int`, `list[str]`)
   - `None` instead of `null`

2. **Pydantic schemas**
   - request/response validation
   - clear data contracts (similar to runtime-validated TypeScript types)

3. **FastAPI dependency injection**
   - `Depends(get_db)` style patterns
   - clean separation of route and service logic

4. **SQLAlchemy session flow**
   - request creates session
   - query/commit/rollback
   - request closes session

### How to learn efficiently (using your existing strengths)

- Build one endpoint in Python the same way you would in Node.
- Compare the same feature across stacks (auth, product CRUD, pagination).
- Keep routes thin and move logic to `services/` (same architectural principle as mature Node apps).
- Use Swagger docs (`/docs`) as your quick feedback loop.

### 7-day practical learning sprint

Day 1:
- Add `GET /api/v1/hello`
- Add query params (`name`, `limit`)

Day 2:
- Create `Product` schema (`ProductCreate`, `ProductRead`)
- Return mock data first

Day 3:
- Create SQLAlchemy `Product` model
- Generate and run Alembic migration

Day 4:
- Add `POST /products` and `GET /products`
- Validate input and return typed responses

Day 5:
- Add error handling (404, validation messages)
- Add pagination and basic filtering

Day 6:
- Add simple auth skeleton (register/login shape)
- Protect one route

Day 7:
- Refactor: route → service → model clarity
- Document what you learned and remaining gaps

If you follow this sprint, you will feel productive quickly because the architecture is already familiar from your Node.js experience.

## Node.js → Python Cheat Sheet (Express/Next API to FastAPI)

Use this section as a quick translation guide while coding.

### 1) Basic route

Node.js (Express):

```js
app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});
```

FastAPI (Python):

```python
@app.get('/health')
def health_check():
   return {'status': 'ok'}
```

### 2) Query parameters

Node.js (Express):

```js
app.get('/products', (req, res) => {
  const limit = Number(req.query.limit ?? 10);
  const search = req.query.search ?? '';
  res.json({ limit, search });
});
```

FastAPI (Python):

```python
from fastapi import Query

@app.get('/products')
def list_products(limit: int = Query(10, ge=1, le=100), search: str = ''):
   return {'limit': limit, 'search': search}
```

### 3) Body validation

Node.js (Express + zod/joi style):

```js
app.post('/products', (req, res) => {
  const { name, price } = req.body;
  if (!name || price == null) return res.status(400).json({ error: 'Invalid body' });
  res.status(201).json({ id: 1, name, price });
});
```

FastAPI (Pydantic):

```python
from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
   name: str = Field(min_length=1)
   price: float = Field(gt=0)

@app.post('/products', status_code=201)
def create_product(payload: ProductCreate):
   return {'id': 1, **payload.model_dump()}
```

### 4) Router modularization

Node.js:

```js
const router = require('express').Router();
router.get('/', listProducts);
app.use('/api/v1/products', router);
```

FastAPI:

```python
from fastapi import APIRouter

router = APIRouter(prefix='/products', tags=['products'])

@router.get('/')
def list_products():
   return []

api_router.include_router(router)
```

### 5) Dependency injection (middleware-like pattern)

Node.js:

```js
app.get('/me', authMiddleware, (req, res) => {
  res.json(req.user);
});
```

FastAPI:

```python
from fastapi import Depends

def get_current_user():
   return {'id': 1, 'email': 'user@example.com'}

@app.get('/me')
def me(current_user = Depends(get_current_user)):
   return current_user
```

### 6) Database session pattern

Node.js (pseudo Prisma/ORM style):

```js
const products = await db.product.findMany();
return res.json(products);
```

FastAPI + SQLAlchemy:

```python
from sqlalchemy.orm import Session
from fastapi import Depends

@router.get('/')
def list_products(db: Session = Depends(get_db)):
   return db.query(Product).all()
```

### 7) Error handling

Node.js:

```js
if (!product) return res.status(404).json({ error: 'Not found' });
```

FastAPI:

```python
from fastapi import HTTPException

if not product:
   raise HTTPException(status_code=404, detail='Not found')
```

### 8) Async mental model

- In Node.js, async is common almost everywhere.
- In FastAPI, you can use either `def` or `async def`.
- Use `async def` when calling async libraries (HTTP clients, async DB drivers).
- Use plain `def` for sync SQLAlchemy patterns like this project currently uses.

### 9) TypeScript mindset transfer

If you are strong in TypeScript, treat Pydantic models as runtime-validated typed contracts.

- `interface Product` mindset → `class ProductRead(BaseModel)`
- `zod schema` mindset → `Field(...)` constraints in Pydantic
- typed service responses → `response_model=ProductRead` in FastAPI routes

### 10) Recommended coding loop for this repo

1. define schema (`schemas/`)
2. add/adjust model (`models/`)
3. write service logic (`services/`)
4. expose route (`api/endpoints/`)
5. register router (`api/router.py`)
6. test quickly in `/docs`

Repeat this loop for each feature until the architecture becomes second nature.
