import sys
import os
import site


in_venv = sys.prefix != sys.base_prefix
venv_path = os.environ.get("VIRTUAL_ENV")
venv_name = os.path.basename(venv_path) if venv_path else None
packages_path = site.getsitepackages()[0]
if in_venv:
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path:{venv_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system")
    print("Package installation path:")
    print(f"{packages_path}")
else:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\activate # On Windows\n")
    print("Then run this program again.")
