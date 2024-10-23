from datetime import datetime, timedelta,timezone
from fastapi import HTTPException, status
import jwt
from config import SECRET_KEY,ALGORITHM


#start creating with token 

from fastapi import FastAPI
app = FastAPI()


@app.get("/generate_token")
def get_token(name:str,email:str):
    payload = {
        "name": name,
        "email": email,
        "exp": datetime.now(timezone.utc) + timedelta(seconds=30),
    }

    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    print(type(access_token))

    return access_token


@app.get("/decode_token")
def decode_token(token:str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        name = payload.get("name")
        email = payload.get("email")
        if not name or not email:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token",
            )
        return {"name": name, "email": email}
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token has expired",
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )
    



#create a dependency for token and access it within new api 
  