from abc import ABC, abstractmethod
from typing import Any, List, Tuple


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"{result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            for element in data:
                if not isinstance(element, int):
                    return False
            return True
        except Exception as e:
            print(f"{e}")
        return False

    def process(self, data: Any) -> str:
        if self.validate(data):
            total = sum(data)
            size = len(data)
            avg = total / size
            return (f"Processed {len(data)} numeric values,"
                    f" sum={total}, avg={avg}")
        return ""


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                return False
            return True
        except Exception as e:
            print(f"{e}")
        return False

    def process(self, data: Any) -> str:
        if self.validate(data):
            tab = data.split(' ')
            count_word = len(tab)
            return (f"Processed text: {len(data)}"
                    f" characters, {count_word} words")
        return ""


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                return False
            if data.startswith("ERROR: ") or data.startswith(
                    "INFO: ") or data.startswith("WARNING: "):
                return True
        except Exception as e:
            print(f"{e}")
        return False

    def process(self, data: Any) -> str:
        if self.validate(data):
            if data.startswith("ERROR: "):
                return f"[ALERT] ERROR level detected {data[7:]}"
            elif data.startswith("INFO: "):
                return f"[INFO] INFO level detected : {data[6:]}"
            elif data.startswith("WARNING: "):
                return f"[WARNING] WARNING level detected {data[9:]}"
        else:
            return "No ERROR message founds"
        return ""


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    num_data: List[int] = [1, 2, 3, 4, 5]
    Nprocessor = NumericProcessor()

    print(f"Processing data: {num_data}")
    num_valid = Nprocessor.validate(num_data)
    print(f"Validation: {'Numeric data verified' if num_valid else None}")
    print(f"Output: Processed {Nprocessor.process(num_data)}")

    print("\nInitializing Text Processor...")
    text_data: str = "prout"
    Tprocessor = TextProcessor()

    print(f"Processing data:'{text_data}'")
    text_valid_bool = Tprocessor.validate(text_data)
    text_valid = (
        'Text data verified' if text_valid_bool else 'Text data is invalid'
    )
    print(f"Validation: {text_valid}")
    text_out = (
        Tprocessor.process(text_data)
        if text_valid_bool else 'Nothing to display'
    )
    print(f"Output: {text_out}")

    print("\nInitializing Log Processor...")
    log_data: str = "WARNING: ffsjfjsf"
    LProcessor = LogProcessor()

    print(f"Processing data: '{log_data}'")
    log_valid = LProcessor.validate(log_data)
    validated = 'Log entry verified' if log_valid else 'No ERROR founds'
    print(f"Validation: {validated}")
    print(f"Output: {LProcessor.process(log_data)}")

    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...\n")
    processors: List[Tuple[DataProcessor, Any]] = [
        (NumericProcessor(), [1, 2, 3, 4, 5]),
        (TextProcessor(), "Hello little world"),
        (LogProcessor(), "ERROR: Connection timeout")
    ]
    for i, (proc, proc_data) in enumerate(processors, start=1):
        proc_result = proc.process(proc_data)
        print(f"Result {i}: {proc.format_output(proc_result)}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")
