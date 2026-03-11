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

    def prime_generator(self):
        n = 2
        while True:
            is_prime = True
            for i in range(2, n):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                yield n
            n += 1

    def fibonacci_generator(self):
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    def generator_demonstration(self, fib_count: int, prime_count: int):
        print("\n=== Generator Demonstration ===")

        fib = self.fibonacci_generator()
        fib_numbers = []
        for _ in range(fib_count):
            fib_numbers.append(next(fib))
        print(
            f"Fibonnaci (First {fib_count}):"
            f"{', '.join(str(n) for n in fib_numbers)}")

        prime = self.prime_generator()
        prime_numbers = []
        for _ in range(prime_count):
            prime_numbers.append(next(prime))
        print(
            f"Prime numbers (first {prime_count}):"
            f"{', '.join(str(n) for n in prime_numbers)}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    wizard = StreamWizard()
    wizard.display_events(5)
    wizard.stream_analytics(100)
    wizard.generator_demonstration(6, 8)
