# Lesson 1: BaseModel & Type Coercion
from typing import Self
from pydantic import BaseModel, ValidationError, Field, EmailStr, field_validator, model_validator

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True
    bio: str | None = None
    
user = User(id="42", name="Rajesh")
print(type(user.model_dump()))

# Lesson 2: Field() Constraints & Nested Models
class OrderItem(BaseModel):
    sku: str = Field(min_length=3, max_length=20)
    qty: int = Field(gt=0, le=100)
    price: float = Field(gt=0)
    
class Order(BaseModel):
    order_id: str
    customer_email: EmailStr
    items: list[OrderItem] = Field(min_length=1)
    
order = Order(
    order_id="ORD-101",
    customer_email="dev@example.com",
    items=[{ "sku": "Laptop-01", "qty": 1, "price": 5000.0 }]
)

# Lesson 3: Custom Validators (@field_validator & @model_validator)
class SignupRequest(BaseModel):
    username: str
    password: str
    confirm_password: str

    @field_validator("username")
    @classmethod # 
    def clean_username(cls, v: str) -> str:
        if " " in v:
            raise ValueError("Username cannot contain spaces")
        return v.strip().lower()

    @model_validator(mode="after")
    def passwords_match(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self