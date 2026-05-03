import os
import datetime
import jwt


def generate_token(user_id):
    secret = os.getenv("AUTH_JWT_SECRET")
    if not secret:
        return None
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=24)
    }
    return jwt.encode(payload, secret, algorithm="HS256")
