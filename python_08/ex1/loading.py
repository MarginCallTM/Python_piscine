import sys
import importlib
import importlib.util


def check_dependencies() -> dict[str, bool]:
    """Check which required packages are installed."""
    packages = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization",
    }
    status: dict[str, bool] = {}
    print("Checking dependencies:")
    for package, description in packages.items():
        spec = importlib.util.find_spec(package)
        if spec is not None:
            mod = importlib.import_module(package)
            version = getattr(mod, "__version__", "unknown")
            print(f"[OK] {package} ({version}) - {description} ready")
            status[package] = True
        else:
            print(f"[MISSING] {package} - {description} not available")
            status[package] = False
    return status


def show_install_instructions() -> None:
    print("\nTo install missing dependencies:")
    print("  With pip:    pip install -r requirements.txt")
    print("  With Poetry: poetry install")
    print("               poetry run python loading.py")


def compare_versions() -> None:
    """Compare installed package versions and detect pip vs Poetry."""
    # Detect tool based on the path of the active Python interpreter
    python_path = sys.executable
    if "pypoetry" in python_path:
        tool = "Poetry"
        tool_info = (
            "Poetry manages a lockfile that pins exact versions.\n"
            "  Every developer gets the exact same environment."
        )
    else:
        tool = "pip"
        tool_info = (
            "pip uses requirements.txt which may allow version ranges.\n"
            "  Different installs may get different versions."
        )

    print(f"\nDependency manager detected: {tool}")
    print(f"  {tool_info}")
    print(f"\nPython interpreter: {python_path}")

    packages = ["pandas", "numpy", "matplotlib"]
    print(f"\n{'Package':<15} {'Version':<15} {'Manager'}")
    print("-" * 45)
    for package in packages:
        spec = importlib.util.find_spec(package)
        if spec is not None:
            mod = importlib.import_module(package)
            version = getattr(mod, "__version__", "unknown")
            print(f"{package:<15} {version:<15} {tool}")
        else:
            print(f"{package:<15} {'NOT INSTALLED':<15}")


def generate_matrix_data() -> "numpy.ndarray":  # type: ignore[name-defined]
    import numpy as np  # noqa: F401
    rng = np.random.default_rng(seed=42)
    data = rng.integers(0, 256, size=(1000, 3))
    return data


# type: ignore[name-defined]
def analyze_data(data: "numpy.ndarray") -> "pandas.DataFrame":
    """Load numpy data into a pandas DataFrame and compute basic stats."""
    import pandas as pd  # noqa: F401
    df = pd.DataFrame(data, columns=["channel_R", "channel_G", "channel_B"])
    print(f"\nProcessing {len(df)} data points...")
    return df


# type: ignore[name-defined]
def generate_visualization(df: "pandas.DataFrame") -> None:
    """Plot the Matrix data and save to matrix_analysis.png."""
    import matplotlib  # noqa: F401
    import matplotlib.pyplot as plt  # noqa: F401
    print("\nGenerating visualization...")
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    colors = ["red", "green", "blue"]
    for i, (col, color) in enumerate(zip(df.columns, colors)):
        axes[i].hist(df[col], bins=30, color=color, alpha=0.7)
        axes[i].set_title(f"Matrix {col}")
        axes[i].set_xlabel("Value")
        axes[i].set_ylabel("Frequency")
    plt.suptitle("Matrix Data Analysis")
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    status = check_dependencies()

    missing = [pkg for pkg, ok in status.items() if not ok]
    if missing:
        show_install_instructions()
        sys.exit(1)

    compare_versions()

    print("\nAnalyzing Matrix data...")
    data = generate_matrix_data()
    df = analyze_data(data)

    generate_visualization(df)

    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()
