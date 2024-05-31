# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count("а"))

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
vowels_count = 0
for ch in word.lower():
    if ch in vowels:
        vowels_count += 1
print(f"количество гласных букв в слове {word} - {vowels_count}")

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(" ")))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for w in sentence.split(" "):
    print(w.capitalize())

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
print(int(sum(len(i) for i in words) / len(words)))
