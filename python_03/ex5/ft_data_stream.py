import random
import time


class StreamWizard:
    def __init__(self):
        pass

    def game_event_stream(self, n):
        players = ["alice", "bob", "charlie"]
        actions = ["Killed monster", "found treasure", "leveled up"]
        for i in range(n):
            yield {
                "id": i + 1,
                "player": random.choice(players),
                "level": random.randint(1, 99),
                "action": random.choice(actions)
            }

    def display_events(self, n):
        print(f"Processing {n} game events...\n")
        for event in self.game_event_stream(n):
            print(
                f"Event {event['id']}: Player {event['player']}"
                f" (level {event['level']}) {event['action']}")

    def stream_analytics(self, n):
        print("\n=== Stream Analytics ===")
        start = time.time()
        total = 0
        high_level = 0
        treasure = 0
        level_up = 0
        for event in self.game_event_stream(n):
            total += 1
            if event['level'] >= 10:
                high_level += 1
            if event['action'] == 'found treasure':
                treasure += 1
            if event['action'] == 'leveled up':
                level_up += 1
        print(f"Total events processed: {total}")
        print(f"High-level players (10+): {high_level}")
        print(f"Treasure events: {treasure}")
        print(f"Level-up events: {level_up}")
        print()
        print("Memory usage: Constant (streaming)")
        end = time.time()
        duration = end - start
        print(f"Processing time: {duration:.3f} seconds")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    wizard = StreamWizard()
    wizard.display_events(5)
    wizard.stream_analytics(1000000)
