import glob
import os
from dataclasses import dataclass

from settings.const import S3

from .base_repostiory import BasePatientRepository


@dataclass
class LocalPatientRepository(BasePatientRepository):
    s3_bucket: str = S3.S3_BUCKETNAME

    def patient_file(self, user_id: str, image_id: str):
        return os.path.join("patient", user_id, image_id)

    def get_image_url(self, user_id: str, image_id: str) -> str:

        return os.path.join(f"/_aws/{self.s3_bucket}", self.patient_file(user_id, image_id))

    def list_image_url(self, user_id: str) -> list[str]:

        return sorted(glob.glob(os.path.join(f"/_aws/{self.s3_bucket}", self.patient_file(user_id, "*"))))

    def post_image(self, content: bytes, user_id: str, image_id: str) -> str:

        path = os.path.join(f"/_aws/{self.s3_bucket}", self.patient_file(user_id, image_id))
        with open(path, "w") as f:
            f.write(content)
        return path.replace("/_aws/", f"{S3.LOCAL_DIR}/")
