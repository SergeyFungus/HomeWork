class WordsFinder:
    def __init__(self, *names):
        self.file_names = []
        for i in names:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for file_names in self.file_names:
            with open(file_names, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for punct in punctuation:
                        line = line.replace(punct, '')
                    for word in line.split():
                        words.append(word)
                all_words[file_names] = words
        return all_words

    def find(self, word):
        places = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                places[key] = value.index(word.lower()) + 1
        return places

    def count(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count

        return counters


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего