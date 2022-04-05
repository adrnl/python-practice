# Your friend is typing his name into a keyboard.
# Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

# You examine the typed characters of the keyboard.
# Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

def isLongPressed(name, typed):
    if name == typed:
        return true

    i, j = 0, 0
    nameLen, typedLen= len(name), len(typed)

    while i < typedLen:
        if j < nameLen and name[j] == typed[i]:
            j += 1
        elif i == 0 or typed[i] != typed[i-1]:
            return False
        i += 1

    return j == nameLen

print(isLongPressed("adrian", "aaddrriiaann"))