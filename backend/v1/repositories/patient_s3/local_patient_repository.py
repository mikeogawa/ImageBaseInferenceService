import glob
import os
from dataclasses import dataclass

from settings.const import S3

from .base_repostiory import BasePatientRepository


@dataclass
class LocalPatientRepository(BasePatientRepository):
    s3_bucket: str = S3.S3_BUCKETNAME

    def cartel_file(self, cartel_id: str, image_id: str):
        return os.path.join("cartel", cartel_id, image_id)

    def get_image_url(self, cartel_id: str, image_id: str) -> str:

        return os.path.join(f"/_aws/{self.s3_bucket}", self.cartel_file(cartel_id, image_id))

    def list_image_url(self, cartel_id: str) -> list[str]:

        return sorted(glob.glob(os.path.join(f"/_aws/{self.s3_bucket}", self.cartel_file(cartel_id, "*"))))

    def post_image(self, content: bytes, cartel_id: str, image_id: str) -> str:

        path = os.path.join(f"/_aws/{self.s3_bucket}", self.cartel_file(cartel_id, image_id))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(content.read())
        return path.replace("/_aws/", f"{S3.LOCAL_DIR}/")
