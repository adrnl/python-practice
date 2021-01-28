def TopKFrequentlyMentioned(reviews, keywords, results):
    if not keywords or not reviews:
        return []
    counters = {}

    for review in reviews:
        review = review.lower()
        for keyword in keywords:
            counters[keyword] = 0
            if keyword.lower() in review:
                counters[keyword] += 1

    solution = sorted(counters.items(), key=lambda counter:(-counter[1], counter[0]))

    return [solution[i][0] for i in range(results)]

reviews = [
    "Anacell provides the best services in the city",
    "betacellular has awesome services",
    "Best services provided by anacell, everyone should use anacell",
]
keywords = ["anacell", "cetracular", "betacellular"]
results = 2
if TopKFrequentlyMentioned(reviews, keywords, results) == ["anacell", "betacellular"]:
    print("Test1 Pass\n")
else:
    print("Test1 Fail:")
    print("    Expected:\n[\"anacell\", \"betacellular\"]")
    print("    Result:")
    print(TopKFrequentlyMentioned(reviews, keywords, results))

reviews = [
    "I love zanacell Best services; Best services provided by zanacell",
    "betacellular has great services",
    "deltacellular provides much better services than betacellular",
    "cetracular is worse than zanacell",
    "Betacellular is better than deltacellular.",
]
keywords = ["zanacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
results = 2
if TopKFrequentlyMentioned(reviews, keywords, results) == ["betacellular", "anacell"]:
    print("Test2 Pass\n")
else:
    print("Test2 Fail:")
    print("    Expected:\n[\"betacellular\", \"anacell\"]")
    print("    Result:")
    print(TopKFrequentlyMentioned(reviews, keywords, results))

# Example 1
# Input:
# k = 2
# keywords = ["anacell", "cetracular", "betacellular"]
# reviews = [
#   "Anacell provides the best services in the city",
#   "betacellular has awesome services",
#   "Best services provided by anacell, everyone should use anacell",
# ]
#
# Output:
# ["anacell", "betacellular"]
#
# Explanation:
# "anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.
#
# Example 2
# Input:
# k = 2
# keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
# reviews = [
#   "I love anacell Best services; Best services provided by anacell",
#   "betacellular has great services",
#   "deltacellular provides much better services than betacellular",
#   "cetracular is worse than anacell",
#   "Betacellular is better than deltacellular.",
# ]
#
# Output:
# ["betacellular", "anacell"]
#
# Explanation:
# "betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews, but "anacell" is lexicographically smaller.