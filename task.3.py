import sys
from pathlib import Path
from colorama import Fore, Style


def show_tree(path, indent=0):
    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(" " * indent + Fore.BLUE + f"📂 {item.name}" + Style.RESET_ALL)
            show_tree(item, indent + 2)
        else:
            print(" " * indent + Fore.GREEN + f"📜 {item.name}" + Style.RESET_ALL)


def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до директорії: python task.3.py /шлях/до/директорії")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + f"Шлях не існує: {path}" + Style.RESET_ALL)
        return
    if not path.is_dir():
        print(Fore.RED + f"Це не директорія, а файл: {path}" + Style.RESET_ALL)
        return

    print(Fore.BLUE + f"📦 {path.name}" + Style.RESET_ALL)
    show_tree(path, indent=2)


if __name__ == "__main__":
    main()