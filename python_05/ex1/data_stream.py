from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Union


class DataStream(ABC):
    def __init__(self, data_batch: list[Any]) -> None:
        self.data_batch = data_batch

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return self.data_batch
        else:
            return [data for data in data_batch if criteria in data]

    def get_stats(self) -> dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "batch_size": len(
                self.data_batch)}


class SensorStream(DataStream):
    def __init__(self, stream_id: str, data_batch: list[Any]) -> None:
        super().__init__(data_batch)
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        count = 0
        avg = 0
        sum_temp = 0
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
                    f"reading processed, avg temp: {avg:.1f}°C\n")
        except ZeroDivisionError as e:
            print(f"{e}")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        base = super().get_stats()
        base.update({"avg_temp": self.avg, "count": self.count})
        return base


class TransactionStream(DataStream):
    def __init__(self, stream_id: str, data_batch: List[Any]) -> None:
        super().__init__(data_batch)
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        count = 0
        buy = 0
        sell = 0
        net_flow = 0

        for data in data_batch:
            value = data.split(":")
            if value[0].startswith("buy"):
                buy += float(value[1])
            elif value[0].startswith("sell"):
                sell += float(value[1])
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
    def __init__(self, stream_id: str, data_batch: List[Any]) -> None:
        super().__init__(data_batch)
        self.stream_id = stream_id

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


if __name__ == "__main__":
    weather = SensorStream(
        "test00", [
            "temp:22.5", "humidity:65", "temp:50", "temp:5", "rain:42"])
    tx = TransactionStream(
        "test01", [
            "buy:100", "sell:150", "buy:75", "sell:200"])
    stream = EventStream("test02", ["login", "error", "logout"])

    run_all = StreamProcessor([weather, tx, stream])
    run_all.process_all()
    run_all.show_stats()
