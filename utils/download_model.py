import requests
from pathlib import Path

def download_file(url, output_path):
    path = Path(output_path)
    if not path.exists():
        print(f"⬇️ Downloading {output_path}...")
        r = requests.get(url)
        r.raise_for_status()
        with open(path, "wb") as f:
            f.write(r.content)
        print("✅ Download complete.")
    else:
        print(f"📦 Using cached file: {output_path}")
