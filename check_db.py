from sqlalchemy import create_engine, inspect
from models import Base

# Create engine
engine = create_engine("sqlite:///./magicAi.db", connect_args={"check_same_thread": False})

# Get inspector
inspector = inspect(engine)

# Get all table names
tables = inspector.get_table_names()

print("Database Tables:")
print("-" * 50)

for table in tables:
    print(f"\n📋 Table: {table}")
    print("  Columns:")
    for column in inspector.get_columns(table):
        print(f"    - {column['name']}: {column['type']}")
    
    # Get indexes
    indexes = inspector.get_indexes(table)
    if indexes:
        print("  Indexes:")
        for index in indexes:
            print(f"    - {index['name']}: {index['column_names']}")
    
    # Get foreign keys
    foreign_keys = inspector.get_foreign_keys(table)
    if foreign_keys:
        print("  Foreign Keys:")
        for fk in foreign_keys:
            print(f"    - {fk['constrained_columns']} -> {fk['referred_table']}.{fk['referred_columns']}") 