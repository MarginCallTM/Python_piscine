from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


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

    def process(self, data: Any) -> str:
        if self.validate(data):
            total = sum(data)
            size = len(data)
            avg = total / size
            return f"Processed {
                len(data)} numeric values, sum={
                sum(data)}, avg={avg}"


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

    def process(self, data: Any) -> str:
        if self.validate(data):
            len(data)
            tab = data.split(' ')
            count_word = len(tab)
            return f"Processed text: {
                len(data)} characters, {count_word} words"


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                return False
            if data.startswith("ERROR: ") or data.startswith("INFO: ") or data.startswith("WARNING: "):
                return True
        except Exception as e:
            print(f"{e}")
        return False
       

    def process(self, data: Any) -> str:
        if self.validate(data):
            if data.startswith("ERROR: "):
                return f"[ALERT] ERROR level detected {data[7:]}"
            elif data.startswith("INFO: "):
                return f"[INFO] INFO level detected : {data[5:]}"
            elif data.startswith("WARNING: "):
                return f"[WARNING] WARNING level detected {data[9:]}"
        else:
            return "No ERROR message founds"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    
    print("Initializing Numeric Processor...")
    data = [1, 2, 3, 4 ,5]
    Nprocessor = NumericProcessor()

    print(f"Processing data: {data}")
    result = Nprocessor.validate(data)
    print(f"Validation: {'Numeric data verified' if result else None}")
    print(f"Output: Processed {Nprocessor.process(data)}")


    print("\nInitializing Text Processor...")
    data = "prout"
    Tprocessor = TextProcessor()

    print(f"Processing data:'{data}'")
    result = Tprocessor.validate(data)
    print(f"Validation: {'Text data verified' if result else 'Text data is invalid'}")
    print(f"Output: {Tprocessor.process(data) if result else 'Nothing to display'}")

    print("\nInitializing Log Processor...")
    data = "WARNING: ffsjfjsf"
    LProcessor = LogProcessor()

    print(f"Processing data: '{data}'")
    result = LProcessor.validate(data)
    print(f"Validation: {'Log entry verified' if result else 'No ERROR founds'}")
    print(f"Output: {LProcessor.process(data)}")

    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...\n")
    processors = [
        (NumericProcessor(), [1, 2, 3, 4, 5]),
        (TextProcessor(), "Hello little world"),
        (LogProcessor(), "ERROR: Connection timeout")
    ]
    for i, (processor, data) in enumerate(processors, start=1):
        result = processor.process(data)
        print(f"Result {i}: {processor.format_output(result)}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")
