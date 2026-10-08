import sys
import importlib

missing_depend: bool = False
libraries: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
}
print("\nREAGENT STATUS: Loading reagents...\n")
print("Checking dependencies:")
for library, description in libraries.items():
    try:
        mod: object = importlib.import_module(library)
        version: str = getattr(mod, "__version__", "unknown")
        print(f"[OK] {library} ({version}) - {description}")
    except ModuleNotFoundError:
        print(f"[MISSING] {library} - Not installed")
        missing_depend = True

if missing_depend is True:
    print("\nMissing dependencies detected!")
    print("Please install required packages:\n")
    print("Using pip:")
    print("  pip install -r ex0/requirements.txt\n")
    print("Using Poetry:")
    print("  poetry install\n")
    sys.exit(1)

import pandas  # noqa: F401, E402
import numpy  # noqa: F401, E402

print("\npip vs Poetry:")
print("  requirements.txt declares what to install;"
      " pip resolves it at install time."
      )
print("  pyproject.toml declares the same constraints,"
      " and Poetry pins the resolved"
      )
print("  versions in poetry.lock so every install is identical.")


print("\nAll reagents present and accounted for.")
