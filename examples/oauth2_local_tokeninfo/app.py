"""
Basic example of a resource server
"""
from pathlib import Path

import connexion

# our hardcoded mock "Bearer" access tokens
TOKENS = {"123": "jdoe", "456": "rms"}


def get_secret(user) -> str:
    return f"You are: {user}"


def token_info(access_token) -> dict:
    uid = TOKENS.get(access_token)
    if not uid:
        return None
    return {"uid": uid, "scope": ["uid"]}


app = connexion.FlaskApp(__name__, specification_dir="spec")
app.add_api("openapi.yaml")
app.add_api("swagger.yaml")


if __name__ == "__main__":
    app.run(f"{Path(__file__).stem}:app", port=8080)
