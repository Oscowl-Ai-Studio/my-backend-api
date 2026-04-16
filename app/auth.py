import os
from datetime import datetime, timedelta
from jose import jwt
from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "my_super_secret_key")
ALGORITHM = "HS256"

# Function to ISSUE tokens
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Middleware for VALIDATION
class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Allow these paths without a token
        allowed_paths = ["/auth/github/login", "/docs", "/openapi.json", "/workspaces/"]
        
        # Only check auth for GET, POST, DELETE etc., except for allowed paths
        if request.url.path in allowed_paths and request.method == "GET":
            return await call_next(request)
            
        if request.url.path in ["/auth/github/login", "/docs", "/openapi.json"]:
            return await call_next(request)

        # Validate token in headers
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid token")

        token = auth_header.split(" ")[1]
        try:
            jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except Exception:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

        return await call_next(request)