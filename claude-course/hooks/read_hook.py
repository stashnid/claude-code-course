# Хук з уроку 12 — блокує читання .env файлів

import sys
import json

def main():
    raw = sys.stdin.read()
    data = json.loads(raw)

    file_path = (
        data.get("tool_input", {}).get("file_path") or
        data.get("tool_input", {}).get("path") or
        ""
    )

    if ".env" in file_path:
        print("Нема проходу", file=sys.stderr)
        sys.exit(2)

    sys.exit(0)

if __name__ == "__main__":
    main()