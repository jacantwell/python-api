from pydantic import BaseModel


# JSON payload containing access token
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
# This can be extended with more fields as needed
class TokenPayload(BaseModel):
    sub: str | None = None
