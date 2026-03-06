import sys


if len(sys.argv) == 1:
    print("No arguments provided!")
else:
    print(f"Arguments received: {len(sys.argv) - 1}")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argument {i}: {arg}")

print(f"Program name: {sys.argv[0]}")
print(f"Total arguments: {len(sys.argv)}")
