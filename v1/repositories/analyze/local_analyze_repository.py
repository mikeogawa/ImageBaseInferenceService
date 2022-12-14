from dataclasses import dataclass

import request

from settings.const import ANALYZE, ENV

from .base_analyze_repository import BasePatientRepository


@dataclass
class LocalAnalyzeRepository(BasePatientRepository):
    analyze_url: str = ANALYZE.URL
    analyze_auth: str = ANALYZE.AUTH

    def run(self, user_id: str, image_id: str):
        if ENV == "local":
            return
        request.post(
            self.analyze_url,
            json={
                "user_id": user_id,
                "image_id": image_id,
            },
            header={
                "API-KEY": self.analyze_auth
            }
        )
