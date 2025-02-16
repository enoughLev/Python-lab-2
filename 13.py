word_numbers_input = input()
word_numbers = [int(x) for x in word_numbers_input.split()]

text = input()

words = text.split()
new_sentence_words = []

for number in word_numbers:
    if 1 <= number <= len(words):
        new_sentence_words.append(words[number - 1])

new_sentence = " ".join(new_sentence_words)
new_sentence = new_sentence[0].upper() + new_sentence[1:]
print(new_sentence)
