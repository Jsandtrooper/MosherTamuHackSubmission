def Ceaser(sentence, numMoves):
    # Sets every number shift above 26 or below -26 between the two numbers.
    while (numMoves > 26):
        numMoves -= 26
    while (numMoves < -26):
        numMoves += 26

    # Initiates some variables.
    encryptedSentence = ''
    space = ' '

    # Creates a standard alphabet dictionary and the encrypted dictionary.
    alphabet = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
        12: "L",
        13: "M",
        14: "N",
        15: "O",
        16: "P",
        17: "Q",
        18: "R",
        19: "S",
        20: "T",
        21: "U",
        22: "V",
        23: "W",
        24: "X",
        25: "Y",
        26: "Z"
    }

    encrypted = {
        "A": 1 + numMoves,
        "B": 2 + numMoves,
        "C": 3 + numMoves,
        "D": 4 + numMoves,
        "E": 5 + numMoves,
        "F": 6 + numMoves,
        "G": 7 + numMoves,
        "H": 8 + numMoves,
        "I": 9 + numMoves,
        "J": 10 + numMoves,
        "K": 11 + numMoves,
        "L": 12 + numMoves,
        "M": 13 + numMoves,
        "N": 14 + numMoves,
        "O": 15 + numMoves,
        "P": 16 + numMoves,
        "Q": 17 + numMoves,
        "R": 18 + numMoves,
        "S": 19 + numMoves,
        "T": 20 + numMoves,
        "U": 21 + numMoves,
        "V": 22 + numMoves,
        "W": 23 + numMoves,
        "X": 24 + numMoves,
        "Y": 25 + numMoves,
        "Z": 26 + numMoves,
    }

    # Encrypts the message by updating the encrypt dictionary values.
    for i in encrypted:
        if encrypted[i] > 26:
            encrypted[i] = encrypted[i] - 26
        elif encrypted[i] < 1:
            encrypted[i] = encrypted[i] + 26

    # Creates the newly encrypted message.
    for letter in sentence:
        if letter == space:
            encryptedSentence += space
        else:
            encryptedLetter = alphabet[encrypted[letter]]
            encryptedSentence += encryptedLetter

    return encryptedSentence

def ReverseLetters(sentence):
    encryptedSentence = ''
    space = ' '

    dict_reverse = {
        "A": "Z",
        "B": "Y",
        "C": "X",
        "D": "W",
        "E": "V",
        "F": "U",
        "G": "T",
        "H": "S",
        "I": "R",
        "J": "Q",
        "K": "P",
        "L": "O",
        "M": "N",
        "N": "M",
        "O": "L",
        "P": "K",
        "Q": "J",
        "R": "I",
        "S": "H",
        "T": "G",
        "U": "F",
        "V": "E",
        "W": "D",
        "X": "C",
        "Y": "B",
        "Z": "A"
    }

    for letter in sentence:
        if letter == space:
            encryptedSentence += space
        else:
            encryptedLetter = dict_reverse[letter]
            encryptedSentence += encryptedLetter

    return encryptedSentence

def OnepadEncode(message,inkey):
    from random import randint
    randomNum = 1
    newMessage = ''
    key = []

    for i in range(len(message)):
        #print(message)
        tempChar = ord(message[i])
        # print(tempChar)
        if ((tempChar >= 97 and tempChar <= 122) or (tempChar >= 65 and tempChar <= 90)):
            randomNum = inkey
            # print(message[i] + " is getting converted by " +str(randomNum) +"\n")
            key.append(randomNum[i])
            # 65-90 A-Z
            # 97-122
            if (tempChar >= 65 and tempChar <= 90):
                if (tempChar + randomNum[i] > 90):
                    tempChar -= 26
                    # print("im fixing myself")
            elif (tempChar >= 97 and tempChar <= 122):
                if (tempChar + randomNum[i] > 122):
                    tempChar -= 26
                    # print("im fixing myself")
            newMessage += chr(tempChar + randomNum[i])
        else:
            newMessage += message[i]
            key.append(-1)
    return newMessage

def Polyalphabetic(message) :
  newMessage = ''
  incrementer = -1
  for i in range(len(message)):
    incrementer+=1
    tempChar = ord(message[i])
    #print(tempChar)
    if((tempChar>= 97 and tempChar<=122) or (tempChar >=65 and tempChar<=90)):
      #65-90 A-Z
      #97-122
      if(tempChar >=65 and tempChar <= 90) :
        if(tempChar+incrementer >90):
          tempChar-=26
          #print("im fixing myself")
      elif(tempChar >=97 and tempChar<=122):
        if(tempChar+i >122):
          tempChar-=26
          #print("im fixing myself")
      newMessage+=chr(tempChar+incrementer)
    else:
      incrementer+=1
      newMessage+= message[i]
  return newMessage

def Columnar(sentence, num_columns):
    #Creates encrypted sentence. This will be returned at the end.
    encryptedSentence = ''

    #Checks if the sentence/phrase contains spaces. Splits into multiple words if true.
    if (' ' in sentence):
        words = sentence.split(' ')

    else:
        words = [sentence]

    #Goes through all the words in the phrase. Can be 1 word, or many.
    for word in words:
        #Empty dictionary used to split letters into columns.
        columns = {
        }

        #Adds lists, or "columns", into the dictionary.
        for i in range(1, num_columns + 1):
            columns[i] = []

        #Resets current column to 0.
        current_column = 0

        #Fills the columns dictionary with letters.
        for letter in word:
            current_column += 1
            if (current_column > num_columns):
                current_column = 1
            if (letter != ' '):
                columns[current_column].append(letter)

        #Creates the encrypted sentence/word by concatenating all the letters in every column.
        for num in columns:
            for letter in columns[num]:
                encryptedSentence += letter

        #Adds spaces at the end of every encrypted word.
        encryptedSentence += " "

    #Removes the very last space, and returns the encrypted phrase.
    encryptedSentence = encryptedSentence[:-1]
    return encryptedSentence

def Piglatin(sentence):
    # Encrypted sentence that will be returned at end of function.
    encrypted_sentence = ''

    # Checks for spaces to see if there is 1 word or multiple.
    if (' ' in sentence):
        words = sentence.split(' ')

    else:
        words = [sentence]

    # Translates every word in list into pig latin.
    for word in words:
        # Resets new_word variable.
        new_word = ''

        # Checks if first letter equals a vowel.
        if (word[0] in ['A', 'E', 'I', 'O', 'U']):
            new_word += word + 'WAY'

        # Checks if first 2 letters are within the following consonant clusters.
        elif (word[0:2] in ['BL', 'BR', 'CH', 'CK', 'CL', 'CR', 'DR', 'FL', 'FR', 'GH', 'GL', 'GR', 'NG', 'PH', 'PL',
                            'PR', 'QU', 'SC', 'SH', 'SK', 'SL', 'SM', 'SN', 'SP', 'ST', 'SW', 'TH', 'TR', 'TW', 'WH',
                            'WR']):

            new_word += word[2:] + word[0:2] + 'AY'

        # Otherwise, treat like a normal word.
        else:
            new_word += word[1:] + word[0] + 'AY'

        encrypted_sentence += new_word + ' '

    encrypted_sentence = encrypted_sentence[:-1]
    return encrypted_sentence


def Emoji(sentence):
    # Initiates some variables.
    encryptedSentence = ''
    space = ' '

    # Creates a standard alphabet dictionary and the encrypted dictionary.
    alphabet = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
        12: "L",
        13: "M",
        14: "N",
        15: "O",
        16: "P",
        17: "Q",
        18: "R",
        19: "S",
        20: "T",
        21: "U",
        22: "V",
        23: "W",
        24: "X",
        25: "Y",
        26: "Z"
    }

    encrypted = {
        "A": '🍎',
        "B": '🍌',
        "C": '😸',
        "D": '🐶',
        "E": '🥚',
        "F": '🏈',
        "G": '🦍',
        "H": '❤',
        "I": '🍦',
        "J": '🃏',
        "K": '🔪',
        "L": '💄',
        "M": '🌜',
        "N": '💅',
        "O": '🍊',
        "P": '🐼',
        "Q": '👑',
        "R": '💍',
        "S": '🐍',
        "T": '⛺️',
        "U": '☔️',
        "V": '🌋',
        "W": '🍉',
        "X": '❌',
        "Y": '🧶',
        "Z": '🦓'
    }

    # Creates the newly encrypted message.
    for letter in sentence:
        if letter == space:
            encryptedSentence += "  "
        else:
            encryptedLetter = encrypted[letter]
            encryptedSentence += encryptedLetter

    return encryptedSentence