import importlib
import types
import sys


def check_package(package: str) -> tuple[bool, str | None]:
    try:
        module: types.ModuleType = importlib.import_module(package)
        version: str = module.__version__
        return True, version
    except ModuleNotFoundError:
        return False, None


if __name__ == "__main__":
    print()
    print("LOADING STATUS: Loading programs ...")
    print()

    print("Checking dependencies:")

    dependencies: list[str] = ["pandas", "numpy", "requests", "matplotlib"]

    missing: bool = False

    description: dict = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready"
        }
    for dependency in dependencies:
        ok: bool
        version: str | None
        ok, version = check_package(dependency)
        if ok:
            print(f"[OK] {dependency} ({version}) - {description[dependency]}")
        else:
            print(f"[ERROR] {dependency} not installed")
            missing = True

    if missing:
        print()
        print("Missing dependencies detected.")
        print("Install them using:")
        print("pip install -r requirements.txt")
        print("poetry install")
        sys.exit(1)

    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore

    data: np.ndarray = np.random.normal(0, 1, 1000)
    df: pd.DataFrame = pd.DataFrame(data, columns=["matrix_signal"])

    print()
    print("Analyzing Matrix data...")
    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")

    plt.plot(df["matrix_signal"])
    plt.title("Matrix Data Analysis")

    filename: str = "matrix_analysis.png"
    plt.savefig(filename)
    plt.close()

    print()
    print("Analysis complete!")
    print(f"Results saved to: {filename}")
