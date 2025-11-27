from abc import ABC, abstractmethod
from typing import Iterable, Dict

class BaseReport(ABC):
    @abstractmethod
    def generate(self, rows: Iterable[Dict]) -> Iterable[Dict]:
        """gen report"""
        raise NotImplementedError
