class Dictionary:
    words = []

    def insert(self):
        word = input("What is your word?")

        if self._word_exists(word):
            print("That word is already defined")
            return

        definition = input("What is the definition of your word?")

        entry = (word, definition)

        self.words.append(entry)

    def lookup(self):
        word = input("What is the word?")

        for entry in self.words:
            if entry[0] == word:
                print("The definition of", word, "is", entry[1])
                return

        print("That is not a word!!!")

    def _word_exists(self, word) -> bool:
        for definition in self.words:
            if definition[0] == word:
                return True
        return False
