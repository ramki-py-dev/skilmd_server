import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv(".env")

SITE_TITLE = "Test"
IS_SWAGGER_ENABLED = os.environ.get("IS_SWAGGER_ENABLED", "true") == "true"

# App URLs
FRONTEND_URL = os.environ.get("frontend_url")
EXTERNAL_APP_URL = os.environ.get("EXTERNAL_APP_URL", FRONTEND_URL)

# Storage
STORAGE_ENVIRONMENT = os.environ.get("STORAGE_ENVIRONMENT", "local")
LOCAL_STORAGE = "local"
AZURE_STORAGE = "azure"
CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
CONTAINER_NAME = os.environ.get("CONTAINER_NAME")


DATABASE_USER_NAME = os.environ.get("DATABASE_USER_NAME")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABASE_PORT = os.environ.get("DATABASE_PORT")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DB_DRIVER_NAME = os.environ.get("DB_DRIVER_NAME")
SSL_CERT_PATH = os.path.abspath(os.getenv("SSL_CERT_PATH", "./DigiCertGlobalRootCA.crt.pem"))

ENV = os.getenv("ENV", "local")

if ENV == "local":
    SQLALCHEMY_DATABASE_URL = (
        f"mysql+pymysql://{DATABASE_USER_NAME}:{quote_plus(DATABASE_PASSWORD)}"
        f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )
else:
    SQLALCHEMY_DATABASE_URL = (
        f"mysql+pymysql://{DATABASE_USER_NAME}:{quote_plus(DATABASE_PASSWORD)}"
        f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
        f"?ssl_ca={SSL_CERT_PATH}&ssl_verify_cert=True"
    )
 

