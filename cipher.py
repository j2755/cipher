

class Caesar:

    def __init__(self, phrase):
        self.phrase = phrase

    def convert_to_list(self):
        string_list = []
        for i in self.phrase:
            string_list.append(i)
        return string_list

    def hasNumbers(self):
        return any(char.isdigit() for char in self.phrase)

    def caesarCipherKey(self, offset=0):
        key = {}
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for letter in alphabet:
            caesar_index = alphabet.index(letter)+offset
            caesar_index = caesar_index % len(alphabet)
            key.update({letter: alphabet[caesar_index]})
        return key

    def encrypt(self, offset):

        if self.hasNumbers() == False:
            key = self.caesarCipherKey(offset)

            fixed_text = self.phrase.upper()
            phrase_split = fixed_text.split()

            new_phrase = []

            for word in phrase_split:
                new_word = ''
                for letter in word:
                    new_letter = key[letter]
                    new_word = new_word+new_letter
                new_phrase.append(new_word)

            complete_encryption = ''
            for word in new_phrase:
                complete_encryption = complete_encryption+' '+str(word)
            return complete_encryption

        else:
            print(self.phrase)
            print("Use a phrase with only letters")

    def ceasarDecryptKey(self, offset):
        key = {}
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for letter in alphabet:
            caesar_index = alphabet.index(letter)+offset
            caesar_index = caesar_index % len(alphabet)
            key.update({alphabet[caesar_index]: letter})
        return key

    def decrypt(self,encrypted_phrase, offset):
    	key = self.ceasarDecryptKey(offset)
    	print(key)
    	fixed_text = encrypted_phrase.upper()
    	phrase_split = fixed_text.split()
    	new_phrase = []
    	for word in phrase_split:
            new_word = ''
            for letter in word:
                new_letter = key[letter]
                new_word = new_word+new_letter
            new_phrase.append(new_word)
            
    	
    	complete_decrypt=''
    	for word in new_phrase:
    		
    		complete_decrypt=complete_decrypt+' '+word
    	
    	return complete_decrypt






