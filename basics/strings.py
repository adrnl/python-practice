# Strings
print("\n String Practice")
phrase = "I'm learning\n:)"
print(phrase + " right?")

# String Functions
print("\n String Functions")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase.index("\n"))
print(phrase.replace("learning", "smarter!"))

# Character Fetching
print("\n Character Fetch")
print(phrase[0])
print(phrase[10])
print(phrase.find("i"))

words = "These ARE WoRdS"
print(words)
words = words.lower()
print(words)
