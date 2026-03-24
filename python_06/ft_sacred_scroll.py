import alchemy

print("=== Sacred Scroll Mastery ===\n")

print("Testing direct module access:")
try:
    fire = alchemy.elements.create_fire()
    print(f"alchemy.elements.create_fire(): {fire}")
    water = alchemy.elements.create_water()
    print(f"alchemy.elements.create_water(): {water}")
    earth = alchemy.elements.create_earth()
    print(f"alchemy.elements.create_earth(): {earth}")
    air = alchemy.elements.create_air()
    print(f"alchemy.elements.create_air(): {air}")
except Exception as e:
    print(e)

print("\nTesting package-level access (controlled by __init__.py):")
try:
    fire = alchemy.create_fire()
    print(f"alchemy.create_fire(): {fire}")
    water = alchemy.create_water()
    print(f"alchemy.create_water(): {water}")
except Exception as e:
    print({e})
try:
    earth = alchemy.create_earth()  # type: ignore
    print(f"alchemy.create_earth(): {earth}")
except Exception:
    print("alchemy.create_earth(): AttributeError - not exposed")
try:
    air = alchemy.create_air()  # type: ignore
    print(f"alchemy.create_air(): {air}")
except Exception:
    print("alchemy.create_air(): AttributeError - not exposed")


print("\nPackage metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")
