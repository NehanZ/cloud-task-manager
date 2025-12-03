import os
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
ENVIRONMENT = os.getenv("NODE_ENV", "development")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set in environment variables")

# Parse the database URL for validation
db_url = urlparse(DATABASE_URL)
if not db_url.scheme.startswith('postgresql'):
    raise ValueError("DATABASE_URL must be a PostgreSQL connection string")

# Production database configuration with connection pooling
engine_config = {
    "pool_size": 10 if ENVIRONMENT == "production" else 5,
    "max_overflow": 20 if ENVIRONMENT == "production" else 10,
    "pool_timeout": 30,
    "pool_recycle": 3600,
    "echo": ENVIRONMENT == "development"
}

engine = create_engine(DATABASE_URL, **engine_config)
meta = MetaData()
conn = engine.connect()

print(f"Database connected in {ENVIRONMENT} mode to: {db_url.netloc}")
