from fastapi import FastAPI, Header, HTTPException
from database import users
from utils import get_user_id_from_token
from logger import log_access  # <-- logging added

app = FastAPI(title="Peloton BOLA – Secure Version")

@app.get("/user/profile/{user_id}")
def get_user_profile(user_id: int, authorization: str = Header(...)):
    if user_id not in users:
        log_access(None, user_id, "Blocked (invalid user)", "secure")
        raise HTTPException(status_code=404, detail="User not found")
    
    requester_id = get_user_id_from_token(authorization)
    if requester_id is None:
        log_access(None, user_id, "Blocked (invalid token)", "secure")
        raise HTTPException(status_code=401, detail="Invalid token")

    if requester_id != user_id:
        log_access(requester_id, user_id, "Blocked (forbidden)", "secure")
        raise HTTPException(status_code=403, detail="Forbidden: You cannot access another user's data")

    log_access(requester_id, user_id, "Allowed", "secure")
    return users[user_id]
