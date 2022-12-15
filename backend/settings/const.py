import json
import os

ENV = "local"


class ANALYZE:
    URL = os.getenv("ANALYZE_URL", "")
    AUTH = os.getenv("ANALYZE_AUTH", "")


class DB:
    DB_NAME = os.getenv("DB_NAME", "")
    DB_USERNAME = os.getenv("DB_USERNAME", "")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_ENDPOINT = os.getenv("DB_ENDPOINT", "")
    DB_PORT = os.getenv("DB_PORT", "")
    ALEMBIC_DB_NAME = os.getenv("ALEMBIC_DB_NAME", "")


class S3:
    S3_BUCKETNAME = os.getenv("S3_BUCKETNAME", "")
    LOCAL_DIR = os.getenv("LOCAL_DIR", "")


class JWT:
    AUTHENTICATION_KEY = os.getenv("AUTHENTICATION_KEY", "")  # "Bearer"
    AUTHENTICATION_KEY_2 = os.getenv("AUTHENTICATION_KEY_2", "")  # "Bearer"
    AUDIENCE = os.getenv("AUDIENCE", "")  # https://some-medical-clinic.auth0.com/api/v2/
    END_POINT = os.getenv("END_POINT", "")  # https://some-medical-clinic.auth0.com/
    ALGORITHM = os.getenv("ALGORITHM", "")  # HRS256"
    VERIFICATION = json.loads(os.getenv("VERIFICATION", "false"))  # True
    LOCAL_SECRET = os.getenv("LOCAL_SECRET", "")  # super-secret


class MACHINEAUTH:
    API_HEADER = os.getenv("MACHINEAUTH_API_HEADER", "")  # "Bearer"
    API_KEY = os.getenv("MACHINEAUTH_API_KEY", "")  # "Bearer"


class DUMMYDATA:
    DOCTOR_SUB_ID = os.getenv("DOCTOR_SUB_ID", "")
    PATIENT_SUB_ID = os.getenv("DOCTOR_SUB_ID", "")
