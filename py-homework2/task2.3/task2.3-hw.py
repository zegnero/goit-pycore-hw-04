import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def visualize_directory(path: Path, indent: str = ""):
    try:
        items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
    except PermissionError:
        print(f"{indent}{Fore.RED}[Доступ заборонено] {path.name}")
        return

    for item in items:
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}📁 {item.name}/")
            visualize_directory(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}📄 {item.name}")

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Вкажіть путь до дерикторії")
        print(f"Приклад дерикторії: python hw03.py /путь/до/директорії")
        sys.exit(1)

    target_path = Path(sys.argv[1])


    if not target_path.exists():
        print(f"{Fore.RED}Помилка: Вказаний путь '{target_path}' не існує.")
        sys.exit(1)

    if not target_path.is_dir():
        print(f"{Fore.RED}Помилка: Вказаний путь '{target_path}' не є директорією.")
        sys.exit(1)

    print(f"\n{Fore.YELLOW}Структура директорії: {target_path.resolve()}\n")
    visualize_directory(target_path)

if __name__ == "__main__":
    main()