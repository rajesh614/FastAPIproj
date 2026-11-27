from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BlogCreate(BaseModel):
    title: str
    slug: str
    content: str | None = None
    author_id: int | None = None


class BlogResponse(BaseModel):
    id: int
    title: str
    slug: str
    content: str | None
    author_id: int | None
    created_at: datetime | None
    is_active: bool | None

    model_config = ConfigDict(from_attributes=True)
