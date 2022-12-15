from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseAnalyzeRepostiory(ABC):

    @abstractmethod
    def run(self, user_id: str, image_id: str) -> str:
        """
        image url
        """
