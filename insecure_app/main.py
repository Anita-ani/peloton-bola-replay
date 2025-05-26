from fastapi import FastAPI, Header, HTTPException
from database import users
from utils import get_user_id_from_token

app = FastAPI(title="Peloton BOLA – Vulnerable Version")

@app.get("/user/profile/{user_id}")
def get_user_profile(user_id: int, authorization: str = Header(...)):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    
    requester_id = get_user_id_from_token(authorization)
    if requester_id is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    # ❌ BOLA Vulnerability – no ownership check
    return users[user_id]
