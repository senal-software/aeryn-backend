# app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings # Import the settings

# Create the SQLAlchemy engine
# `pool_pre_ping=True` checks connections for liveness before handing them out
# `echo=True` logs SQL queries (useful for debugging, disable in production)
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
    # echo=True # Uncomment for debugging SQL
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative class definitions
Base = declarative_base()

# Optional: Function to create tables (useful for initial setup without migrations)
# def init_db():
#     # Import all modules here that might define models so that
#     # they will be registered properly on the metadata. Otherwise
#     # you will have to import them first before calling init_db()
#     # import app.models.account  # Example import
#     # import app.models.item    # Example import
#     print("Creating database tables...")
#     Base.metadata.create_all(bind=engine)
#     print("Database tables created.")