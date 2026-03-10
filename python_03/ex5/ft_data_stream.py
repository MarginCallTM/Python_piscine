import random


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
        print(f"Processing {n} game events...")
        for event in self.game_event_stream(n):
            print(
                f"Event {event['id']}: Player {event['player']}"
                f" (level {event['level']}) {event['action']}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    wizard = StreamWizard()
    wizard.display_events(20)
