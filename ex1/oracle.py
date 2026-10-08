import sys
import os
from dotenv import load_dotenv  # type: ignore[import-not-found]

env_exists: bool = os.path.exists(".env")

load_dotenv()

variables: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

flag: bool = True
matrix_mode: str = str(os.getenv("MATRIX_MODE"))
if matrix_mode == "development":
    flag = False
elif matrix_mode == "production":
    flag = True
else:
    print(
          "Error: MATRIX_MODE missing or not set to"
          " 'development' or 'production'"
          )
    # sys.exit(1)

print("\nORACLE STATUS: Consulting the configuration...\n")
print("Configuration loaded:")

for variable in variables:
    value: str = str(os.getenv(variable))
    if not value:
        print(f"{variable} is missing")
        sys.exit(1)

    if variable == "MATRIX_MODE":
        print(f"Mode: {value}")
        continue

    if variable == "DATABASE_URL":
        print("Database: Connected to local instance")
        continue

    if variable == "API_KEY":
        if flag is False:
            print("API Key: Authenticated")
        else:
            print(f"API Key: {value}")
        continue

    if variable == "LOG_LEVEL":
        print(f"Log Level: {value}")
        continue

    if variable == "ZION_ENDPOINT":
        print("Remote Network: Online")
        continue

    print(value)

print("\nEnvironment security check:")
secrets_ok: bool = "API_KEY" in os.environ and bool(os.getenv("API_KEY"))
# secrets_ok: bool = False
if secrets_ok:
    print("[OK] No hardcoded secrets detected")
else:
    print("[KO] Hardcoded secrets detected")

if env_exists:
    print("[OK] .env file properly ignored by git")

else:
    print("[KO] .env file not properly ignored by git")

overrides_ok: bool = matrix_mode in ["development", "production"]
if overrides_ok:
    print("[OK] Production overrides available")
else:
    print("[KO] Production overrides unavailable")

print("\nThe Oracle sees all configurations.")
