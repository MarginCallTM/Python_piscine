from functools import wraps
from collections.abc import Callable
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get('power', args[0])
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying..."
                        f" (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            c.isalpha() or c == ' ' for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str) -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball("dragon")
    print(f"Result: {result}\n")

    print("Testing retrying spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise ValueError("Spell unstable!")

    print(unstable_spell())

    @retry_spell(max_attempts=3)
    def stable_spell() -> str:
        return "Waaaaaagh spelled !"

    print(stable_spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("AB"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", power=15))
    print(guild.cast_spell("Lightning", power=5))
