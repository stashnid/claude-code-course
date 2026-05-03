# Приклад з уроку 14 — запуск Claude програматично

import subprocess

def ask_claude(prompt: str) -> str:
    result = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def main():
    response = ask_claude("Explain what CLAUDE.md is in one sentence")
    print("Claude відповів:", response)

if __name__ == "__main__":
    main()