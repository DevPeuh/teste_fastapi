from pydantic import BaseModel
from datetime import datetime, UTC

class PostOut(BaseModel):
    title: str
    #authot: str
    date: datetime
    #published_at: datetime = datetime.now(UTC)