from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import Index

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String)  # Nullable for Google users
    
    # Profile
    profile_picture = Column(String)
    bio = Column(String)
    
    # Authentication
    google_id = Column(String, unique=True)  # For Google Sign-In
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    
    # Credits
    credits = Column(Float, default=10.0)
    lifetime_credits = Column(Float, default=10.0)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime)
    
    # Relationships
    tool_usage = relationship("UserToolUsage", back_populates="user")
    ad_views = relationship("AdView", back_populates="user")
    credit_transactions = relationship("CreditTransaction", back_populates="user")

class Tool(Base):
    __tablename__ = 'tools'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
    credit_cost = Column(Float, nullable=False)
    ad_duration = Column(Integer, nullable=False)  # Duration in seconds
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class UserToolUsage(Base):
    __tablename__ = 'user_tool_usage'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    tool_id = Column(Integer, ForeignKey('tools.id'))
    credits_spent = Column(Float, nullable=False)
    used_at = Column(DateTime, default=datetime.utcnow)
    success = Column(Boolean, default=True)
    error_message = Column(Text, nullable=True)

    user = relationship("User", back_populates="tool_usage")

class AdView(Base):
    __tablename__ = 'ad_views'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    ad_type = Column(String(20), nullable=False)  # 'daily', 'tool', etc.
    credits_earned = Column(Float, nullable=False)
    viewed_at = Column(DateTime, default=datetime.utcnow)
    completed = Column(Boolean, default=False)
    completion_time = Column(DateTime, nullable=True)
    
    user = relationship("User", back_populates="ad_views")

class CreditTransaction(Base):
    __tablename__ = 'credit_transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float, nullable=False)
    transaction_type = Column(String(20), nullable=False)  # 'ad_reward', 'tool_usage', 'admin', etc.
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="credit_transactions")

class Prompt(Base):
    __tablename__ = 'prompts'

    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    description = Column(String, nullable=True)
    creator_id = Column(String, index=True)

# Create indexes for better query performance
Index('idx_user_email', User.email)
Index('idx_user_google_id', User.google_id)
Index('idx_tool_usage_user_id', UserToolUsage.user_id)
Index('idx_ad_views_user_id', AdView.user_id)
Index('idx_credit_transactions_user_id', CreditTransaction.user_id)
