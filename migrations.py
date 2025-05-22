"""
Database migration script for AI Tool Hub
"""
import os
from sqlalchemy import create_engine
from models import Base

def run_migrations():
    """Run database migrations"""
    # Get database URL from environment or use default
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./magicAi.db")
    
    # Create engine
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    
    try:
        # Drop all existing tables
        Base.metadata.drop_all(bind=engine)
        print("✓ Dropped existing tables")
        
        # Create all tables
        Base.metadata.create_all(bind=engine)
        print("✓ Created new tables")
        
        print("\nMigration completed successfully!")
        
    except Exception as e:
        print(f"\nError during migration: {str(e)}")
        raise

if __name__ == "__main__":
    # Confirm with user before proceeding
    print("WARNING: This will delete all existing data. Are you sure? (y/N)")
    response = input().lower()
    
    if response == 'y':
        run_migrations()
    else:
        print("Migration cancelled.") 