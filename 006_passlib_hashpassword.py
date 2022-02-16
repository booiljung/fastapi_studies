#!/bin/python3
# pip3 install fastapi uvicorn[standard] pydantic python-jose[cryptography] passlib[bcrypt]

import sys
from datetime import datetime, timedelta
from passlib.context import CryptContext

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

if len(sys.argv) == 1:
    print("password required")
    exit()
print(get_password_hash(sys.argv[1]))