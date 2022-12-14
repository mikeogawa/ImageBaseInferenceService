from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BasePatientRepository(ABC):

    @abstractmethod
    def get_image_url(self, user_id: str, image_id: str) -> str:
        """
        image url
        """

    @abstractmethod
    def list_image_url(self, user_id: str) -> list[str]:
        """
        list of image url
        """

    @abstractmethod
    def post_image(self, content: bytes, user_id: str, image_id: str):
        """
        post iimage
        """
