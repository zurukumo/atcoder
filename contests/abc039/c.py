S = input()

keyboard = "WBWBWWBWBWBW" * 2
tone = ["Do", "", "Re", "", "Mi", "Fa", "", "So", "", "La", "", "Si"]

print(tone[keyboard.find(S[:12])])
