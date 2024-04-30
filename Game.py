import random
from os import path


class Game:

    file_name = "words.txt"
    level = 1# 1-> Easy, 2 -> Medium, 3 -> Hard (not defined the logic)
    lives = 6

    def run_game(self):
        """
        Method where the game is defined
        :return:
        """
        count = 1
        try:
            while True:
                print("Select a level [1 -> Easy, 2 -> Medium]\n")
                print(f"Lives remaining: {self.lives}")
                n = input("Select a level from the given list: [1, 2]: ")
                if (n == "1") or (n == "2"):
                    print("Selected Level: " + str(n), end="\n\n")
                    break
                else:
                    print("Invalid choice: " + str(n), end="\n\n")
                print("#############################################\n")

            word_to_find = self.__get_word_from_file__().lower()
            #print("Word: " + word_to_find)
            word_with_missing_letters = self.remove_letters_randomly(word_to_find, n)
            print("Guess Word: " + word_with_missing_letters)
            while True:

                guess = input("Guess a letter (a - z): ")
                if len(word_to_find ) == len(word_with_missing_letters):
                    if guess in word_to_find:
                        for i in range(len(word_to_find)):
                            if word_to_find[i] == guess:
                                word_with_missing_letters = self.replace_with_letter(word_with_missing_letters, guess, i)

                    else:
                        self.lives -= 1
                        print(f"Lost a life.. Lives remaining. {self.lives}\n")
                    if (word_to_find == word_with_missing_letters) and (self.lives > 0):
                        print("You have found the word. YOU HAVE WON !!!")
                        break
                    elif self.lives == 0:
                        print("Lives are over. YOU LOST !!!")
                        print(f"\n The Word was {word_to_find}")
                        break
                    print(f"Found Word: {word_with_missing_letters}\n")
                    count += 1
                else:
                    raise Exception("Problem with selected word. Start the game once more..")



        except Exception as e:
            print(e)

    def replace_with_letter(self, word, letter, index):
        string_list = list(word)
        string_list[index] = letter

        return "".join(string_list)


    def remove_letters_randomly (self, word, level):
        """
        Method to remove the letters randomly from the selected word
        :param word:
        :return:
        """
        res_word = ""
        miss_letter_list = []
        word_len = len(word)
        miss_len = 0
        try:
            # Here the number of missing letters should be defined based on level chosen
            if level == "1":
                miss_len = int(word_len/2)
            elif level == "2":
                miss_len = int(word_len/2) + 1

            # Generate list of random indices (with word length)
            # using which the letters in the word should be replaced
            while miss_len > len(miss_letter_list):
                miss_letter_list = []
                for i in range(0, miss_len):
                    n = random.randint(0, word_len - 1)

                    if n not in miss_letter_list:
                        miss_letter_list.append(n)

            string_list = list(word)
            for i in miss_letter_list:
                string_list[i] = "_"

            res_word = "".join(string_list)
        except Exception as e:
            print(e)

        return res_word

    def __read_text_file__(self):
        """
        Method to read the text file
        :return:
        """
        content = []
        main_content = []
        try:
            if path.exists(self.file_name):
                with open(self.file_name, 'r') as f:
                    content = f.read().splitlines()

            for word in content:
                if len(word) > 3:
                    main_content.append(word)

        except Exception as e:
            print(e)

        return main_content

    def __get_word_from_file__(self):
        """
        Method to get a random word from word text file
        :return:
        """
        content = self.__read_text_file__()
        content_length = len(content)
        random_index = random.randint(0, content_length - 1)

        return content[random_index]


if __name__ == '__main__':
    print('#####################################\n')
    print('Starting Hangman Game\n')
    print('#####################################\n')
    game = Game()
    game.run_game()
