from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Union
from typing import Protocol, runtime_checkable


@runtime_checkable
class ProcessingStage(Protocol):

    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages = []

    def add_stage(self, stage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class InputStage():

    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        if isinstance(data, (str, dict, list)):
            return True

    def process(self, data: Any) -> Any:
        if self.validate(data):
            return data
        else:
            return None


class TransformStage():

    def process(self, data: Any) -> Any:
        if isinstance(data, str):
            return f"Transformed: {data}"
        elif isinstance(data, list):
            element = "processed"
            data.append(element)
            return data
        elif isinstance(data, dict):
            data["status"] = "processed"
            return data


class OutputStage():

    def process(self, data: Any) -> Any:
        if not data:
            return "Error"
        else:
            return f"Output: {data}"


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        result = data
        for stage in self.stages:
            result = stage.process(result)
        return result


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        result = data
        for stage in self.stages:
            result = stage.process(result)
        return f"CSV | {result}"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipline_id: str):
        super().__init__()
        self.pipeline_id = pipline_id
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        result = data
        for stage in self.stages:
            result = stage.process(result)
        return f"Stream summary {result}"


class NexusManager():
    def __init__(self, pipline_id: str):
        super().__init__()
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())
    
	def add_pipelines():
        pass
    
	def process_data():
        pass


if __name__ == "__main__":
    test = InputStage()

    print(test.process("temp:22.5"))
    print(test.process(None))

    trans = TransformStage()

    print(trans.process("Temp:22.5"))
    print(trans.process(["test1", "test2", 42]))
    print(trans.process({"sensor": "temp", "value": 22.5}))

    output = OutputStage()

    print(output.process("Temp:25"))
    print(output.process([["test1", "test2", 42]]))
    print(output.process({"sensor": "temp", "value": 22.5}))
    print(output.process(None))

    json_pipe = JSONAdapter("JSON_001")
    print(json_pipe.process('{"sensor": "temp", "value": 22.5}'))

    csv = CSVAdapter("CSV_002")
    print(csv.process("Temp: 42"))

    stream = StreamAdapter("Stream_003")
    print(stream.process("Real-time sensor stream"))
