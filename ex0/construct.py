import sys
import site
import os

if __name__ == "__main__":
    package_paths: list[str] = site.getsitepackages()
    if sys.prefix != sys.base_prefix:
        env_name: str = os.path.basename(sys.prefix)
        print("LABORATORY STATUS: You are working in the open\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install reagents without affecting"
              "the global system.\n"
              )
        print(f"Reagent installation path: {package_paths[0]}")
    else:
        print("LABORATORY STATUS: The laboratory is sealed\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("Every reagent you install here leaks into the whole system.\n")
        print("To seal the laboratory, run:")
        print("python -m venv <lab_env>")
        print("source <lab_env>/bin/activate # On Unix")
        print("<lab_env>\\Scripts\activate # On Windows\n")
        print("Then run this program again.")
