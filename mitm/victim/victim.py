import time
import requests

URL = "http://10.10.0.30:8080/flag"

while True:
    print("[Victim] Requesting flag...", flush=True)

    try:
        response = requests.get(URL, timeout=3)
        print(response.text, flush=True)
    except Exception as e:
        print(f"[Victim] Request failed: {e}", flush=True)

    print("-------------------------", flush=True)

    time.sleep(5)