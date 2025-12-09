from pydantic import BaseModel
from datetime import datetime, UTC

class PostOut(BaseModel):
    title: str
    authot: str
    published_at = datetime = datetime.now(UTC)