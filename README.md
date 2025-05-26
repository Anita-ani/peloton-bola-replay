# Peloton BOLA Replay Lab

This project simulates a real-world API vulnerability (BOLA - Broken Object Level Authorization) inspired by the Peloton API breach. It includes both a **vulnerable version** and a **secure version** side by side for education, testing, and training.

## 🔐 Secure vs 🔓 Insecure Apps

| App            | Port  | Behavior                                    |
|----------------|-------|---------------------------------------------|
| `insecure_app` | 8000  | Vulnerable: Any user can access any profile |
| `secure_app`   | 8001  | Secure: Only profile owner can access data  |

## 📂 Structure

- `insecure_app/` — vulnerable logic
- `secure_app/` — secure logic
- `logger.py` — logs access attempts
- `access.log` — audit trail

## ▶️ How to Run

### . Install requirements
```bash
pip install -r requirements.txt


-Run insecure version
cd insecure_app
uvicorn main:app --reload --port 8000

-Run secure version
cd ../secure_app
uvicorn main:app --reload --port 8001

Test both insecure and secure using:
curl http://localhost:8000/user/profile/2 -H "authorization: user-1"   # ✅ Vulnerable
curl http://localhost:8001/user/profile/2 -H "authorization: user-1"   # ❌ Blocked


🔒 Security Notice
This app is for educational use only and should never be deployed in a production environment.



MIT License

Copyright (c) 2025 Anita

Permission is hereby granted, free of charge, to any person obtaining a copy...
