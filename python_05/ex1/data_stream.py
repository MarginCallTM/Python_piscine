from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Union


class DataStream(ABC):
    def __init__(self, data_batch: Optional[List[Any]] = None) -> None:
        self.data_batch = data_batch if data_batch is not None else []
        self.stream_id: str = ""
        self.stream_type: str = ""
        self.stream_label: str = ""
        self.stream_name: str = ""

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> Union[List[Any], str]:
        if not criteria:
            return self.data_batch
        else:
            return [data for data in data_batch if criteria in data]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_type": self.stream_type,
            "stream_name": self.stream_name,
            "stream_id": self.stream_id,
            "batch_size": len(self.data_batch)}


class SensorStream(DataStream):
    def __init__(self, stream_id: str,
                 data_batch: Optional[List[Any]] = None) -> None:
        super().__init__(data_batch)
        self.stream_id = stream_id
        self.stream_type = "Environmental Data"
        self.stream_label = "readings processed"
        self.stream_name = "Sensor data"

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> Union[List[Any], str]:
        tmp_alert = []
        for data in data_batch:
            value = data.split(":")
            if value[0].startswith("temp"):
                tmp_value = float(value[1])
                if tmp_value > 50:
                    tmp_alert.append(tmp_value)
        if len(tmp_alert) > 0:
            return f"{len(tmp_alert)} critical sensor alerts,"
        else:
            return ""

    def process_batch(self, data_batch: List[Any]) -> str:
        count = 0
        sum_temp: float = 0.0
        count_temp = 0
        try:
            for data in data_batch:
                if isinstance(data, str):
                    value = data.split(":")
                    if value[0].startswith("temp"):
                        sum_temp += float(value[1])
                        count_temp += 1
                    count += 1
            avg = sum_temp / count_temp
            self.avg = avg
            self.count = count
            return (f"Sensor analysis: {count}"
                    f" readings processed, avg temp: {avg:.1f}°C\n")
        except ZeroDivisionError:
            self.avg = 0.0
            self.count = 0
            return "Sensor analysis: no temperature data found\n"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        base = super().get_stats()
        base.update({"avg_temp": self.avg, "count": self.count})
        return base


class TransactionStream(DataStream):
    def __init__(self, stream_id: str,
                 data_batch: Optional[List[Any]] = None) -> None:
        super().__init__(data_batch)
        self.stream_id = stream_id
        self.stream_type = "Financial Data"
        self.stream_label = "operations processed"
        self.stream_name = "Transaction data"

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> Union[List[Any], str]:
        tx_alert = []
        for data in data_batch:
            value = data.split(":")
            if value[0].startswith("buy") or value[0].startswith("sell"):
                tx_value = int(value[1])
                if tx_value > 500:
                    tx_alert.append(tx_value)
        if len(tx_alert) > 0:
            return f"{len(tx_alert)} large transaction,"
        else:
            return ""

    def process_batch(self, data_batch: List[Any]) -> str:
        count = 0
        buy = 0
        sell = 0

        for data in data_batch:
            value = data.split(":")
            if value[0].startswith("buy"):
                buy += int(value[1])
            elif value[0].startswith("sell"):
                sell += int(value[1])
            count += 1
        net_flow = buy - sell
        sign = "+" if net_flow >= 0 else "-"
        self.net_flow = net_flow
        self.count = count
        return (
            f"Transaction analysis: {count} operations, "
            f"net flow: {sign}{abs(net_flow)} units\n"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        base = super().get_stats()
        base.update({"net_flow": self.net_flow, "count": self.count})
        return base


class EventStream(DataStream):
    def __init__(self, stream_id: str,
                 data_batch: Optional[List[Any]] = None) -> None:
        super().__init__(data_batch)
        self.stream_id = stream_id
        self.stream_type = "System Data"
        self.stream_label = "events processed"
        self.stream_name = "Event data"

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None) -> Union[List[Any], str]:
        error_alert = []
        for data in data_batch:
            if data.startswith("error"):
                error_alert.append(data)
        if len(error_alert) > 0:
            return f"{len(error_alert)} critical Error log alerts,"
        else:
            return ""

    def process_batch(self, data_batch: List[Any]) -> str:
        count = 0
        error = 0
        for data in data_batch:
            if data.startswith("error"):
                error += 1
            count += 1
        self.count = count
        self.error = error
        return f"Event analysis: {count} events, {error} error detected\n"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        base = super().get_stats()
        base.update({"error": self.error, "count": self.count})
        return base


class StreamProcessor():
    def __init__(self, list_stream: List[DataStream]) -> None:
        self.list_stream = list_stream

    def process_all(self) -> None:
        for stream in self.list_stream:
            print(f"{stream.process_batch(stream.data_batch)}")

    def show_stats(self) -> None:
        for stream in self.list_stream:
            print(f"{stream.get_stats()}")

    def summary_stats(self) -> None:
        print("Batch 1 Results:")
        lst = []
        for data in self.list_stream:
            stats = data.get_stats()
            print(
                f"- {stats['stream_name']}: {stats['count']}"
                f" {data.stream_label}")
            lst.append(str(data.filter_data(data.data_batch)))
        print("Stream filtering active: High-priority data only")
        print(f"Filtered results: {' '.join(lst)}")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    weather = SensorStream("SENSOR_001", sensor_batch)
    print(f"Stream ID: {weather.stream_id}, Type: {weather.stream_type}")
    print(f"Processing sensor batch: [{', '.join(sensor_batch)}]")
    print(weather.process_batch(sensor_batch))

    print("Initializing Transaction Stream...")
    tx_batch = ["buy:100", "sell:150", "buy:75"]
    tx = TransactionStream("TRANS_001", tx_batch)
    print(f"Stream ID: {tx.stream_id}, Type: {tx.stream_type}")
    print(f"Processing transaction batch: [{', '.join(tx_batch)}]")
    print(tx.process_batch(tx_batch))

    print("Initializing Event Stream...")
    event_batch = ["login", "error", "logout"]
    event = EventStream("EVENT_001", event_batch)
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print(f"Processing event batch: [{', '.join(event_batch)}]")
    print(event.process_batch(event_batch))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    run_all = StreamProcessor([weather, tx, event])
    run_all.summary_stats()

    print("\nAll streams processed successfully. Nexus throughput optimal.")
