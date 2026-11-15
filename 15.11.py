sentence = input("Enter a sentence: ").lower()

freq = {}
for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    print(word, "→", count)