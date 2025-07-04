from abc import ABC, abstractmethod
from typing import Any, List, Type


class Processor(ABC):
    """Интерфейс процессора изображения."""

    dependencies: List[Type["Processor"]] = []

    def __init__(self, name: str = ''):
        self.name = name or self.__class__.__name__

    @abstractmethod
    def process(self, image: Any) -> Any:
        pass

    def metadata_status_value(self) -> str:
        return "True"
