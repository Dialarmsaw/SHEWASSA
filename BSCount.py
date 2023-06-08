import keyboard
backspaceCount = 0

while keyboard.read_key()!="home":
    if keyboard.read_key() == "f19":
        backspaceCount += 1
print(backspaceCount)
