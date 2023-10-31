"""Settings."""
import os

SMTP_HOST = "localhost"
SMTP_PORT = 8025
SMTP_TIMEOUT = 10

EMAIL_FROM = "master@dundie.example.com"
DATEFMT: str = "%d/%m/%Y %H:%M:%S"
API_BASE_URL = "https://economia.awesomeapi.com.br/json/last/USD-{currency}"

ROOT_PATH = os.path.dirname(__file__)
DATABASE_PATH = os.path.join(ROOT_PATH, "..", "assets", "database.db")

SQL_CONN_STRING = f"sqlite:///{DATABASE_PATH}"
