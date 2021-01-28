# One example would be to take this paragraph of text
# and return a list of alphabetized unique words.
# After each word tell me how many times the word appeared
# and in what sentance(s) the word appreared in.

def coallate(input):
    count = {}
    if not input:
        return count
    input = input.lower()
    words = input.split(" ")
    words.sort()
    for word in words:
        if word in count.keys():
            count[word] += 1
        else:
            count[word] = 1

    return count


input = "This is a collection of words. These words will be turned into a list of alphabetized UNIQUE words. Emphasis " \
        "on the unique part of that. Then for every word, there will be a count for how many times the word appeared, " \
        "and if I get ambitious, it will tell you which sentences the word appeared in."
print(coallate(input))
