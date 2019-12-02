#Written by: (Six-S)
#Challenge #380 Smooshed Morse Code 1
#https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/

class Morse():
    def __init__(self):
        #a-z in morse code.
        #include '' to handle sentences.
        self.morse_list = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 
            'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 
            'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 
            'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
            'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
            'z': '--..', '': ''
        }

        #Grab our file, and put it into memory for us to mess with later.
        #This is for the optional bonus challenges.
        f = open('enable1.txt', 'r')
        self.text = f.readlines()
        print (self.text)
        f.close()

    #Get the word we're going to encode, immedietly convert to lowercase
    def get_word(self):
        return input('Word to encode: ').lower()

    #Encode word into morse code
    def encode_word(self, word_to_encode):
        #Make sure we have everything
        if self.empty(word_to_encode):
            word = list(word_to_encode)
            encoded_word = ''
            for letter in word:
                #Encode word letter by letter from morse list.
                encoded_word = encoded_word + self.morse_list[letter]
            #return the word we built
            return encoded_word

    #Find values that repeat more than once in the list.
    def find_repeated_codes(self):
        raise NotImplementedError
        for word in self.morse_list:
            encoded_word = self.encode_word(word)

    #Utility function to test for empty variables
    def empty(self, value):
        try:
            value = float(value)
        except ValueError:
            pass
        return bool(value)

if __name__ in '__main__':
    challenge = Morse()

    #Challenge 1
    word = challenge.get_word()
    print(challenge.encode_word(word))

    #Challenge 3


