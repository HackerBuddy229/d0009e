class Dictionary:
    words = {}

    def insert(self):
        word = input("What is your word?")

        if self._word_exists(word):
            print("That word is already defined")
            return

        definition = input("What is the definition of your word?")

        self.words[word] = definition

    def lookup(self):
        word = input("What is the word?")

        if word in self.words:
            print("The definition of", word, "is", self.words[word])
            return

        print("That is not a word!!!")

    def _word_exists(self, word) -> bool:
        return word in self.words
