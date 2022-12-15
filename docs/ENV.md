```bash
# ANALYZE:
ANALYZE_URL="http://backend:8000/"
ANALYZE_AUTH="machine_key"


# DB:
DB_NAME=some_medical_service
DB_USERNAME=admin
DB_PASSWORD=password
DB_ENDPOINT=db
DB_PORT=5432
ALEMBIC_DB_NAME=alembic


# S3 (set your local)
S3_BUCKETNAME=some-medical-clinic
LOCAL_DIR= # Insert the current directory of this file


# JWT:
AUTHENTICATION_KEY=Bearer
AUTHENTICATION_KEY_2=Bearer2
AUDIENCE=https://some-medical-clinic.auth0.com/api/v2/
END_POINT=https://some-medical-clinic.auth0.com/
ALGORITHM=HS256
VERIFICATION=true
LOCAL_SECRET=super-secret


# MACHINEAUTH:
MACHINEAUTH_API_HEADER=API-KEY # "Bearer"
MACHINEAUTH_API_KEY=SOME_MACHINE_KEY # "Bearer"

# DummyData
DOCTOR="auth0|3425c05d168e1f0d69f0361"
PATIENT="auth0|1120c06d167e2a00697f0312"
```