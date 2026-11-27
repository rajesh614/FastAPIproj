from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    blogs = relationship("Blog", back_populates="author")
