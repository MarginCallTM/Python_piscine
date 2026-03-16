from abc import ABC, abstractmethod


class processor(ABC):
    @abstractmethod
    def process(self, data: str) -> str:
        pass


class UpperProcessor(processor):
    def process(self, data: str) -> str:
        result = data.upper()
        return result


class ReverseProcessor(processor):
    def process(self, data: str) -> str:
        result = data[::-1]
        return result


class LenghtProcessor(processor):
    def process(self, data: str) -> str:
        return f"Lengh -> {len(data)}"


def run_all(processors: list, data: str) -> None:
    for processor in processors:
        print(processor.process(data))


if __name__ == "__main__":
    run_all([UpperProcessor(), ReverseProcessor(), LenghtProcessor()], "Hello")