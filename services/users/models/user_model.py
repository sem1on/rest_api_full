from pydantic import BaseModel, field_validator


class UserModel(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int


    @field_validator("id", "username","email", "username")
    def field_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value