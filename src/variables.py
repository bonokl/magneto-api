import os

from dotenv import load_dotenv

load_dotenv()
database_url: str = os.environ.get("DATABASE_URL", None)
base_url: str = os.environ.get("BASE_URL", "/v1/magneto")
docs_user: str = os.environ.get("DOCS_USER", "admin")
docs_password: str = os.environ.get("DOCS_PASSWORD", "admin")
debug = (os.environ.get("DEBUG", "False")).lower() in ('true', 'yes', 't', 'y', '1')
host = os.environ.get("HOST", "0.0.0.0")
port = int(os.environ.get("PORT", "8195"))
log_level = os.environ.get("LOG_LEVEL", "debug")
