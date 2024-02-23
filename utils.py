import json
from base64 import b64encode

import config


def generate_token(payload: dict) -> str:
    pretoken = b64encode(json.dumps(payload).encode()).decode()
    s_key_len = len(config.SECRET_KEY)
    token = b64encode(
        (
            config.SECRET_KEY[:s_key_len] + pretoken + config.SECRET_KEY[s_key_len:]
        ).encode()
    ).decode()
    return token
