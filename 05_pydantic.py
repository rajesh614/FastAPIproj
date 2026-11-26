from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional 
from enum import Enum
from datetime import datetime

class Language(str, Enum):
    PY = "python"
    JAVA = "java"
    GO = "go"

class Blog(BaseModel):
    title: str
    description: Optional[str] = None
    is_active: bool
    language: Language = Language.PY
    created_at: datetime = Field(default_factory=datetime.now)
    
first_blog = Blog(title="My title", is_active=True)
print (first_blog)

import time
time.sleep(5)

second_blog = Blog(title="My title", is_active=True)
print (second_blog)

class CreateUser(BaseModel):
    email: str
    password: str
    confirm_password: str
    
    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if "admin" in value:
            raise ValueError("This email is not allowed")
        return value
    
    @model_validator(mode="after")
    def passwords_match(self) -> "CreateUser":
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
    
CreateUser(email="rajesh@gmail.com", password="123", confirm_password="123")
