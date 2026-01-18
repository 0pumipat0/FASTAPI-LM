from pydantic import BaseModel

class depressionRequest(BaseModel):
    query: str
    type: str
    top_k: int