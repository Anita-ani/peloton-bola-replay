import logging
from datetime import datetime

# Basic file logger
logging.basicConfig(
    filename="access.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_access(requester_id: int, target_id: int, outcome: str, app: str):
    logging.info(
        f"[{app}] Requester user-{requester_id} -> user-{target_id} | Result: {outcome}"
    )
