# Digitador Gago

corrected_words = []
franciscos_sentence = input().split()

for word in franciscos_sentence:
    if len(word) > 3 and word[:2] == word[2:4]:
        word = word[:2] + word[4:]
    corrected_words.append(word)

corrected_line = ' '.join(corrected_words)
print(corrected_line)
