import jwt
from passlib.context import CryptContext
import datetime

SECRET_KEY = "secret"
ALGORITHM = "HS256"

salt = CryptContext(schemes=["bcrypt"])

def hash_password(password: str):
    return salt.hash(password)

def check_password(password: str, hashed: str):
    return salt.verify(password, hashed)

def create_token(user_id: int):
    payload = {
        "user_id": user_id,
        "issue_At":int(datetime.datetime.now().timestamp())
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)