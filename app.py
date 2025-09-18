# vulnerable_secret_example.py

import os

# ❌ Hardcoded secret in source — this will be committed to VCS if not removed
API_KEY = "AKIA12345EXAMPLESECRETKEY"

def initialize():
    # ❌ Writing secret into environment at runtime from code
    #    (still keeps the secret in repo history and makes detection harder)
    os.environ["MY_APP_API_KEY"] = API_KEY

if __name__ == "__main__":
    initialize()
    print("API key loaded into environment (insecure).")
