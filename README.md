# Credit Card Fraud Detection API

A production-style REST API that serves real-time credit-card fraud predictions from a trained machine-learning model, with JWT authentication, a PostgreSQL backend, and full Docker Compose orchestration.

Built with FastAPI, scikit-learn, and PostgreSQL. Containerized end to end.

---

## What it does

- **Live fraud scoring** — POST a transaction, get back a fraud prediction and probability from a trained model.
- **Authentication** — user registration and login with hashed passwords (bcrypt) and JWT access tokens.
- **Analytics endpoints** — transaction counts, fraud rate, top-risk transactions, and high-risk-hour aggregation, backed by PostgreSQL.
- **Fully containerized** — API and database run together via Docker Compose; one command to start the whole stack.

---

## Tech stack

| Layer | Technology |
|---|---|
| API framework | FastAPI |
| ML | scikit-learn (Logistic Regression, Decision Tree) |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Auth | JWT (python-jose), bcrypt (passlib) |
| Validation | Pydantic |
| Containerization | Docker, Docker Compose |

---

## The model

Trained on the Kaggle credit-card fraud dataset (284,807 transactions, ~0.17% fraud — a heavily imbalanced problem).

**Approach**
- Stratified train/test split to preserve the tiny fraud proportion in both sets.
- Compared Logistic Regression and a Decision Tree.
- Evaluated on **precision, recall, and AUPRC** rather than accuracy — accuracy is misleading at a 0.17% base rate, where predicting "never fraud" scores ~99.8%.

**Results (fraud class, Logistic Regression — selected model)**

| Metric | Score |
|---|---|
| Precision | 0.83 |
| Recall | 0.70 |
| F1 | 0.76 |

Logistic Regression was chosen over the Decision Tree, which reached the same precision but lower recall (0.64).

---

## Running it

### With Docker Compose (recommended)

```bash
git clone https://github.com/bhaskardey02/fastapi-learning.git
cd fastapi-learning
docker compose up --build
```

The API comes up at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

### Environment

Secrets are read from environment variables / a `.env` file (not committed). Required:

```
SECRET_KEY=<your-secret>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Key endpoints

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | `/auth/register` | Create a user | No |
| POST | `/auth/login` | Get a JWT token | No |
| POST | `/predict/` | Score a transaction for fraud | No |
| GET | `/transactions/count` | Total transactions | No |
| GET | `/frauds/count` | Total fraud transactions | No |
| GET | `/fraud/percentage` | Fraud rate | No |
| GET | `/frauds/top10` | Highest-value frauds | No |
| GET | `/hours/high-risk` | Fraud by hour of day | No |
| GET | `/stats` | Aggregate fraud statistics | JWT |

### Example: predict

```bash
POST /predict/
{
  "Time": 406.0, "V1": -2.31, "V2": 1.95, ... "Amount": 0.0, "Hour": 0, "HighValue": 0
}

# Response
{ "prediction": 1, "fraud_probability": 0.64 }
```

---

## Project structure

```
app/
  main.py            # app entry, router registration
  database.py        # SQLAlchemy engine + session
  models.py          # ORM models (User, CreditCardTransaction)
  schemas.py         # Pydantic request/response schemas
  crud.py            # database queries
  auth.py            # password hashing, JWT create/verify
  config.py          # settings via pydantic-settings
  ml_model.py        # loads the trained model
  models/            # saved .joblib model artifact
  routers/
    auth.py          # register / login
    fraud.py         # analytics endpoints
    predict.py       # ML prediction endpoint
Dockerfile
docker-compose.yml
requirements.txt
```

---

## Notes & next steps

- Model artifacts are versioned with the code; in a larger system these would live in object storage or a model registry.
- Planned: automated tests (pytest), async endpoints, and CI.
