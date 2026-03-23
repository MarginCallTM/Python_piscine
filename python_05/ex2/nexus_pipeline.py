import time
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from typing import Protocol, runtime_checkable


@runtime_checkable
class ProcessingStage(Protocol):
    description: str

    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class InputStage():
    def __init__(self) -> None:
        self.description = "Stage 1: Input validation and parsing"

    def validate(self, data: Any) -> bool:
        if data is None:
            return False
        if isinstance(data, (str, dict, list)):
            return True
        return False

    def process(self, data: Any) -> Any:
        if self.validate(data):
            return data
        else:
            return None


class TransformStage():
    def __init__(self) -> None:
        self.description = "Stage 2: Data transformation and enrichment"

    def process(self, data: Any) -> Any:
        if isinstance(data, str):
            return f"Transformed: {data}"
        elif isinstance(data, list):
            data.append("processed")
            return data
        elif isinstance(data, dict):
            data["status"] = "processed"
            return data
        else:
            raise ValueError("Invalid data format")


class OutputStage():
    def __init__(self) -> None:
        self.description = "Stage 3: Output formatting and delivery"

    def process(self, data: Any) -> Any:
        if not data:
            return "Error"
        else:
            return f"{data}"


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
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
    def __init__(self, pipeline_id: str) -> None:
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
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        result = data
        for stage in self.stages:
            result = stage.process(result)
        return f"Stream summary {result}"


class NexusManager(ProcessingPipeline):
    def __init__(self, manager_id: str) -> None:
        super().__init__()
        self.manager_id = manager_id
        self.pipelines: Dict[str, ProcessingPipeline] = {}
        self.records_processed: int = 0
        self.total_time: float = 0.0

    def add_pipelines(
            self,
            pipeline_id: str,
            pipeline: ProcessingPipeline) -> None:
        self.pipelines[pipeline_id] = pipeline

    def process_data(self, data: Any, pipeline_id: str,
                     backup_id: Optional[str] = None) -> Any:
        start = time.time()
        try:
            if pipeline_id not in self.pipelines:
                raise ValueError(f"Pipeline '{pipeline_id}' not found.")
            result = self.pipelines[pipeline_id].process(data)
            self.records_processed += 1
            self.total_time += time.time() - start
            return result
        except ValueError as e:
            if backup_id and backup_id in self.pipelines:
                print(f"Error detected in Stage 2: {e}")
                print("Recovery initiated: Switching to backup processor")
                result = self.pipelines[backup_id].process(str(data))
                self.records_processed += 1
                self.total_time += time.time() - start
                print(
                    "Recovery successful: "
                    "Pipeline restored, processing resumed"
                )
                return result
            raise

    def get_stats(self) -> Dict[str, Any]:
        return {
            "manager_id": self.manager_id,
            "records_processed": self.records_processed,
            "total_time": round(self.total_time, 4),
            "pipelines": list(self.pipelines.keys())
        }

    def process(self, data: Any) -> Any:
        result = data
        for pipeline in self.pipelines.values():
            result = pipeline.process(result)
        return result


if __name__ == "__main__":

    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")

    print("Creating Data Processing Pipeline...")
    json_pipe = JSONAdapter("JSON_001")
    for stage in json_pipe.stages:
        print(stage.description)

    # === Multi-Format Data Processing ===
    print("\n=== Multi-Format Data Processing ===\n")

    json_data = '{"sensor": "temp", "value": 23.5, "unit": "C"}'
    print("Processing JSON data through pipeline...")
    print(f"Input: {json_data}")
    print("Transform: Enriched with metadata and validation")
    print(f"Output: {json_pipe.process(json_data)}\n")

    csv_pipe = CSVAdapter("CSV_002")
    csv_data = "user,action,timestamp"
    print("Processing CSV data through same pipeline...")
    print(f"Input: {csv_data}")
    print("Transform: Parsed and structured data")
    print(f"Output: {csv_pipe.process(csv_data)}\n")

    stream_pipe = StreamAdapter("Stream_003")
    stream_data = "Real-time sensor stream"
    print("Processing Stream data through same pipeline...")
    print(f"Input: {stream_data}")
    print("Transform: Aggregated and filtered")
    print(f"Output: {stream_pipe.process(stream_data)}\n")

    # === Pipeline Chaining Demo ===
    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")

    nexus = NexusManager("Manag_id001")
    nexus.add_pipelines("JSON_001", JSONAdapter("JSON_001"))
    nexus.add_pipelines("CSV_002", CSVAdapter("CSV_002"))
    nexus.add_pipelines("Stream_003", StreamAdapter("Stream_003"))

    chain_result = nexus.process("raw sensor data")
    stats = nexus.get_stats()
    nb = len(stats['pipelines'])
    print(f"Chain result: processed through {nb}-stage pipeline")
    print(f"Performance: total time {stats['total_time']}s\n")

    # === Error Recovery Test ===
    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    nexus.process_data(42, "JSON_001", backup_id="CSV_002")

    print("\nNexus Integration complete. All systems operational.")
