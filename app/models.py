from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)
    password = Column(String)  # Add password field
    created_at = Column(DateTime, server_default=func.now())

    # Optional: Add a relationship to appointments (if you want appointments later)
    # appointments = relationship("Appointment", back_populates="user")
