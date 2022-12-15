import jwt
from settings.const import DUMMYDATA, JWT, MACHINEAUTH

key = JWT.LOCAL_SECRET


def make_user(sub, type_):
    payload = {
        "id": "1",
        'aud': JWT.AUDIENCE,
        'iss': JWT.END_POINT,
        'sub': sub,
        "app_meta": {"type": type_},
    }
    print("--->", JWT.ALGORITHM)
    return jwt.encode(payload, key, algorithm=JWT.ALGORITHM)


def main():
    doctor_token = make_user(DUMMYDATA.DOCTOR_SUB_ID, "doctor")
    patient_token = make_user(DUMMYDATA.PATIENT_SUB_ID, "patient")
    machine_key = MACHINEAUTH.API_KEY
    print("patient:", patient_token)
    print("doctor:", doctor_token)
    print("machine:", machine_key)


if __name__ == "__main__":
    main()
