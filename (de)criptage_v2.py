def cryptage(text, number):  
    sentence = ''
    number %=  26
    for letter in text:
        if letter in alphabet:
            final_number = alphabet.index(letter) + number
            sentence += (alphabet[final_number%26])
        elif letter in special_chars:
                sentence += (letter)
        elif letter in char_map.keys():
            sentence += (char_map[letter])
        else:
            print(f'Erreur caractère non convertissable : {letter}')
            sentence += letter
    return sentence

                    
def option_morse(text):
    sentence_morse = ''
    for letter in text:
        if letter in alphabet:
            sentence_morse += (morse_alphabet[alphabet.index(letter)])
        elif letter in char_map:
            sentence_morse += (morse_alphabet[alphabet.index(char_map[letter])])
        elif letter in special_chars:
            sentence_morse += (special_to_morse[letter])
        else:
            print(f'Erreur caractère non convertissable : {letter}')
            sentence_morse += letter
    return sentence_morse


def morse_trad(text):
    translated_sentence = ""
    list = text.split(' ')
    for letter in list:
        if letter in morse_alphabet:
            translated_sentence += (alphabet[morse_alphabet.index(letter)])
        elif letter in morse_to_special.keys():
            translated_sentence += (morse_to_special[letter])
        else:
            print(f'Erreur caractère non convertissable : {letter}')
            translated_sentence += letter
        print(f'Le texte traduit est "{translated_sentence}"')
    return translated_sentence


def decryptage(text, number):
    cryptage(text,-number)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

char_map = {
    'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
    'à': 'a', 'ù': 'u', 'ç': 'c', 'ô': 'o',
    'ï': 'i', 'î': 'i'
}

special_chars = set(' .,:;?!\'"*1234567890%/+-=_()@#$°£<>€&')

chiffre = set('0123456789')

morse_alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..',
                  '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
                  '-.--', '--..']

special_to_morse = {
    ' ': '/', '1': '.----', '2': '..---', '3': '...--','4': '....-','5': '.....','6': '-....','7': '--...',
    '8': '---..','9': '----.','0': '-----','.': '.-.-.-',',': '--..--','?': '..--..',"'": ".----.",'!': '-.-.--','/': '-..-.','(': '-.--.',
    ')': '-.--.-','&': '.-...',':': '---...',';': '-.-.-.','+': '.-.-.','-': '-....-','=': '-...-','_': '..-.-','"': '.-..-.','$': '...-..-','@': '.--.-.'
}

morse_to_special = {value: key for key, value in special_to_morse.items()} #inverse les keys et valeur du dictionnaire précédent

question1 = input('Souhaitez vous déchiffer ou crypter un texte?'
                  ' Veuillez répondre "d" pour déchifrer ou "c" pour crypter. ').lower()
while question1 != 'c' and question1 != 'd':
    print('Réponse non valide')
    question1 = input('Souhaitez vous déchiffer ou crypter un texte?'
                      ' Veuillez répondre "d" pour déchifrer ou "c" pour crypter. ').lower()
else:
    text = input('Entrer votre texte : ').lower()  
    if question1 == 'c':
        q_cesar = input('Voulez-vous cripter ce texte en language '
                    'de César ou chiffrement par décalage? (oui/non) ').lower()
        while q_cesar != 'non' and q_cesar != 'oui':
                print('Réponse non valide')
                q_cesar = input('Voulez-vous cripter ce texte en language '
                                'de César ou chiffrement par décalage? (oui/non) ').lower()
        else:
            if q_cesar == 'oui':
                number = input('Entrer le nombre : ')
                while not(number in chiffre):
                    print("Nombre invalide.")
                    number = input('Entrer le nombre : ')
                int(number)
                text = cryptage(text, number)
                print(f'Le texte codé est "{text}"')

            q_m = input('Voulez-vous traduire ce texte en morse? (oui/non) ').lower()
            while q_m != 'oui' and q_m != 'non':
                print('Réponse non valide')
                q_m = input('Voulez-vous traduire ce texte en morse? (oui/non) ').lower()
            else:
                if q_m == 'oui':
                    text = option_morse(text)
                    print(f'Le texte en morse est "{text}"')

    else:
        q_m = input("Voulez-vous traduire ce texte du morse vers l'alphabet latin? (oui/non) ").lower()
        while q_m != 'oui' and q_m != 'non':
            print('Réponse non valide')
            q_m = input("Voulez-vous traduire ce texte du morse vers l'alphabet latin? (oui/non) ").lower()
        else:
            if q_m == 'oui':
                text = morse_trad(text)

        q_d1 = input('Voulez-vous décripter/chiffrer ce texte en language'
                 ' de César ou chiffrement par décalage? (oui/non) ').lower()
        while q_d1 != 'oui' and q_d1 != 'non':
            print('Réponse non valide')
            q_d1 = input('Voulez-vous décripter ce texte en language'
                        'de César ou chiffrement par décalage? (oui/non) ').lower()
        else:
            if q_d1 == 'oui':
                print('Sachez que le décodage soustrait le nombre donné (exemple: si nombre = 3'
                  ' alors erqmrxu devient bonjour.')
                q_d2 = input('Connaissez vous le nombre permettant le déchiffrage?'
                              ' Veuillez répondre par oui ou par non. ').lower()
                while q_d2 != 'oui' and q_d2 != 'non':
                    print('Réponse non valide')
                    print('Avant tout sachez que le décodage soustrait le nombre donné (exemple: si nombre = 3'
                  ' alors erqmrxu devient bonjour.')
                    q_d2 = input('Connaissez vous le nombre permettant le décodage? '
                                    'Veuillez répondre par oui ou par non. ').lower()
                else:
                    if q_d2 == 'oui':
                        
                        number = input('Entrer le nombre : ')
                        while not(number in chiffre):
                            print("Nombre invalide.")
                            number = input('Entrer le nombre : ')
                        int(number)
                        text = decryptage(text,number)
                        print(f'Le texte décodé est "{text}"')
                    else:
                        for i in range (25):
                            print(f'Le texte codé est "{decryptage(text,i+1)}"')