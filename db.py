from models import Base
from sqlalchemy import create_engine

engine = create_engine("sqlite:///magicAi.db")
Base.metadata.create_all(bind=engine)