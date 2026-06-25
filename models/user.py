from pydantic import BaseModel


class UserCreate(BaseModel):

    username: str

    user_email: str

    password: str

    role: str
