def searchSuggestions(products, searchWord):
    products.sort()
    current = ""
    suggestions = []
    for char in searchWord:
        suggestion = []
        current += char
        for product in products:
            if product.startswith(current) and len(suggestion) < 3:
                suggestion.append(product)

        suggestions.append(suggestion)

    print(suggestions)
    return suggestions

items = ["mobile","mouse","moneypot","monitor","mousepad"]
word = "mouse"
if searchSuggestions(items, word) == [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]:
    print("Test1 PASS")
else:
    print("Test1 FAIL")

items = ["havana"]
word = "havana"
if searchSuggestions(items, word) == [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]:
    print("Test2 PASS")
else:
    print("Test2 FAIL")

items = ["bags","baggage","banner","box","cloths"]
word = "bags"
if searchSuggestions(items, word) == [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]:
    print("Test3 PASS")
else:
    print("Test3 FAIL")

items = ["havana"]
word = "tatiana"
if searchSuggestions(items, word) == [[],[],[],[],[],[],[]]:
    print("Test4 PASS")
else:
    print("Test4 FAIL")

# go through each character, get prefixes, continue

# Given an array of strings products and a string searchWord.
# We want to design a system that suggests at most three product names from products after each character of searchWord is typed.
# Suggested products should have common prefix with the searchWord.
# If there are more than three products with a common prefix return the three lexicographically minimums products.
#
# Return list of lists of the suggested products after each character of searchWord is typed.
#
# Example 1:
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
#
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
#
# Example 2:
# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
#
# Example 3:
# Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
# Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
#
# Example 4:
# Input: products = ["havana"], searchWord = "tatiana"
# Output: [[],[],[],[],[],[],[]]
#
# Constraints:
# 1 <= products.length <= 1000
# There are no repeated elements in products.
# 1 <= Σ products[i].length <= 2 * 10^4
# All characters of products[i] are lower-case English letters.
# 1 <= searchWord.length <= 1000
# All characters of searchWord are lower-case English letters.