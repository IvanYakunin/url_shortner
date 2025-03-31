from pydantic import BaseModel, EmailStr
from datetime import datetime

class LongUrlDC(BaseModel):
    url: str

class CreateShortUrlDC(BaseModel):
    url: str
    expiresAt: datetime = None
    alias: str = ""

class ShortUrlDC(BaseModel):
    url: str

class ShortUrlStatsDC(BaseModel):
    originalUrl: str
    visits: int
    lastTimeUsed: datetime
    createdAt: datetime

class UpdateUrlDC(BaseModel):
    newUrl: str

class UserCreateDC(BaseModel):
    email: EmailStr
    password: str

class TokenDC(BaseModel):
    access_token: str
    token_type: str = "bearer"