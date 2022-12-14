import os
from dataclasses import dataclass, field

import boto3

from settings.const import S3

from .base_repostiory import BasePatientRepository


@dataclass
class S3PatientRepository(BasePatientRepository):
    s3_bucket: str = S3.S3_BUCKETNAME
    _client: boto3.client = field(init=False, repr=False)

    @property
    def clent(self):
        if not getattr(self, "_client"):
            self._client = boto3.Session().client("s3")
        return self._client

    def patient_file(self, user_id: str, image_id: str):
        return os.path.join("patient", user_id, image_id)

    def get_image_url(self, user_id: str, image_id: str) -> str:

        res = self.client.generate_presigned_url(
            'get_object',
            Params=dict(
                Bucket=self.s3_bucket,
                Key=self.patient_file(user_id, image_id),
                ExpiresIn=3600
            )
        )
        return res

    def list_image_url(self, user_id: str) -> list[str]:
        result = self.client.list_objects_v2(
            Bucket=self.s3_bucket,
            Prefix=self.patient_file(user_id, ""),
            Delimiter='/',
        )
        res = []
        for o in result.get('CommonPrefixes'):
            res.append(o.get('Prefix'))
        return sorted([self.get_image_url(s) for s in res])

    def post_image(self, content: bytes, user_id: str, image_id: str) -> str:
        key = self.patient_file(user_id, image_id)
        self.clent.put_object(
            Body=content,
            Bucket=self.s3_bucket,
            Key=key,
        )

        return os.path.join("s3://", self.s3_bucket, key)
