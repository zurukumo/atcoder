import colorama


def print_red(text: str) -> None:
    print(colorama.Fore.RED + text + colorama.Style.RESET_ALL)


def print_yellow(text: str) -> None:
    print(colorama.Fore.YELLOW + text + colorama.Style.RESET_ALL)


def print_green(text: str) -> None:
    print(colorama.Fore.GREEN + text + colorama.Style.RESET_ALL)
