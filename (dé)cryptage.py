def cryptage():
    text = input('Entrer votre texte').lower()
    q_cesar = input('Voulez-vous cripter ce texte en language '
                    'de César ou chiffrement par décalage? (oui/non)').lower()
    while q_cesar != 'non' and q_cesar != 'oui':
        print('Réponse non valide')
        q_cesar = input('Voulez-vous cripter ce texte en language '
                        'de César ou chiffrement par décalage? (oui/non)').lower()
    else:
        if q_cesar == 'oui':
            number = int(input('Entrer le nombre.'))
            final_list_c = []
            number = number % 26
            for letter in text:
                if letter in alphabet:
                    verification_number = 0
                    while letter != alphabet[verification_number]:
                        verification_number += 1
                    else:
                        final_number = verification_number + number
                        if final_number > 25:
                            final_number -= 26
                            final_list_c.append(alphabet[final_number])
                        else:
                            final_list_c.append(alphabet[final_number])
                else:
                    if letter == ' ':
                        final_list_c.append(' ')
                    elif letter == '.':
                        final_list_c.append('.')
                    elif letter == ':':
                        final_list_c.append(':')
                    elif letter == ';':
                        final_list_c.append(';')
                    elif letter == ',':
                        final_list_c.append(',')
                    elif letter == '?':
                        final_list_c.append('?')
                    elif letter == '!':
                        final_list_c.append('!')
                    elif letter == "'":
                        final_list_c.append("'")
                    elif letter == '"':
                        final_list_c.append('"')
                    elif letter == '*':
                        final_list_c.append('*')
                    elif letter == '1':
                        final_list_c.append('1')
                    elif letter == '2':
                        final_list_c.append('2')
                    elif letter == '3':
                        final_list_c.append('3')
                    elif letter == '4':
                        final_list_c.append('4')
                    elif letter == '5':
                        final_list_c.append('5')
                    elif letter == '6':
                        final_list_c.append('6')
                    elif letter == '7':
                        final_list_c.append('7')
                    elif letter == '8':
                        final_list_c.append('8')
                    elif letter == '9':
                        final_list_c.append('9')
                    elif letter == '0':
                        final_list_c.append('0')
                    elif letter == '%':
                        final_list_c.append('%')
                    elif letter == '/':
                        final_list_c.append('/')
                    elif letter == '+':
                        final_list_c.append('+')
                    elif letter == '-':
                        final_list_c.append('-')
                    elif letter == '=':
                        final_list_c.append('=')
                    elif letter == '_':
                        final_list_c.append('_')
                    elif letter == '(':
                        final_list_c.append('(')
                    elif letter == ')':
                        final_list_c.append(')')
                    elif letter == '@':
                        final_list_c.append('@')
                    elif letter == '#':
                        final_list_c.append('#')
                    elif letter == '$':
                        final_list_c.append('$')
                    elif letter == '°':
                        final_list_c.append('°')
                    elif letter == '£':
                        final_list_c.append('£')
                    elif letter == '<':
                        final_list_c.append('<')
                    elif letter == '>':
                        final_list_c.append('>')
                    elif letter == '&':
                        final_list_c.append('&')
                    elif letter == '€':
                        final_list_c.append('€')
                    elif letter == 'é':
                        final_list_c.append('e')
                    elif letter == 'è':
                        final_list_c.append('e')
                    elif letter == 'ê':
                        final_list_c.append('e')
                    elif letter == 'ë':
                        final_list_c.append('e')
                    elif letter == 'à':
                        final_list_c.append('a')
                    elif letter == 'ù':
                        final_list_c.append('u')
                    elif letter == 'ç':
                        final_list_c.append('c')
                    elif letter == 'ô':
                        final_list_c.append('o')
                    elif letter == 'ï':
                        final_list_c.append('i')
                    elif letter == 'î':
                        final_list_c.append('i')
                    else:
                        print(f'error: {letter}')
            final_sentence_c = ''.join(final_list_c)
            print(f'Le texte codé est "{final_sentence_c}"')
            print(option_morse(final_sentence_c))
        if q_cesar == 'non':
            print(option_morse(text))


def option_morse(x):
    list_morse_caratere = []
    question_morse = input('Voulez-vous transcrire ce texte en morse? (oui/non)').lower()
    while question_morse != 'non' and question_morse != 'oui':
        print('Réponse non valide')
        question_morse = input('Voulez-vous transcrire ce texte en morse? (oui/non)').lower()
    else:
        if question_morse == 'oui':
            for letter in x:
                if letter in alphabet:
                    verification_number = 0
                    while letter != alphabet[verification_number]:
                        verification_number += 1
                    else:
                        list_morse_caratere.append(morse_alphabet[verification_number])
                else:
                    if letter == ' ':
                        list_morse_caratere.append('/')
                    elif letter == '1':
                        list_morse_caratere.append('.----')
                    elif letter == '2':
                        list_morse_caratere.append('..---')
                    elif letter == '3':
                        list_morse_caratere.append('...--')
                    elif letter == '4':
                        list_morse_caratere.append('....-')
                    elif letter == '5':
                        list_morse_caratere.append('.....')
                    elif letter == '6':
                        list_morse_caratere.append('-....')
                    elif letter == '7':
                        list_morse_caratere.append('--...')
                    elif letter == '8':
                        list_morse_caratere.append('---..')
                    elif letter == '9':
                        list_morse_caratere.append('----.')
                    elif letter == '0':
                        list_morse_caratere.append('-----')
                    elif letter == '.':
                        list_morse_caratere.append('.-.-.-')
                    elif letter == ',':
                        list_morse_caratere.append('--..--')
                    elif letter == '?':
                        list_morse_caratere.append('..--..')
                    elif letter == "'":
                        list_morse_caratere.append(".----.")
                    elif letter == '!':
                        list_morse_caratere.append('-.-.--')
                    elif letter == '/':
                        list_morse_caratere.append('-..-.')
                    elif letter == '(':
                        list_morse_caratere.append('-.--.')
                    elif letter == ')':
                        list_morse_caratere.append('-.--.-')
                    elif letter == '&':
                        list_morse_caratere.append('.-...')
                    elif letter == ':':
                        list_morse_caratere.append('---...')
                    elif letter == ';':
                        list_morse_caratere.append('-.-.-.')
                    elif letter == '+':
                        list_morse_caratere.append('.-.-.')
                    elif letter == '-':
                        list_morse_caratere.append('-....-')
                    elif letter == '=':
                        list_morse_caratere.append('-...-')
                    elif letter == '_':
                        list_morse_caratere.append('..-.-')
                    elif letter == '"':
                        list_morse_caratere.append('.-..-.')
                    elif letter == '$':
                        list_morse_caratere.append('...-..-')
                    elif letter == '@':
                        list_morse_caratere.append('.--.-.')
                    elif letter == 'é':
                        list_morse_caratere.append('.')
                    elif letter == 'è':
                        list_morse_caratere.append('.')
                    elif letter == 'ê':
                        list_morse_caratere.append('.')
                    elif letter == 'ë':
                        list_morse_caratere.append('.')
                    elif letter == 'à':
                        list_morse_caratere.append('.-')
                    elif letter == 'ù':
                        list_morse_caratere.append('..-')
                    elif letter == 'ç':
                        list_morse_caratere.append('-.-.')
                    elif letter == 'ô':
                        list_morse_caratere.append('---')
                    elif letter == 'ï':
                        list_morse_caratere.append('..')
                    elif letter == 'î':
                        list_morse_caratere.append('..')
                    else:
                        print(f'error: {letter}')
            sentence_morse = ' '.join(list_morse_caratere)
            print(f'Le texte en morse est "{sentence_morse}"')


def decryptage():
    print(morse_trad())
    q_d1 = input('Voulez-vous décripter ce texte en language'
                 ' de César ou chiffrement par décalage? (oui/non)').lower()
    while q_d1 != 'oui' and q_d1 != 'non':
        print('Réponse non valide')
        q_d1 = input('Voulez-vous décripter ce texte en language'
                     'de César ou chiffrement par décalage? (oui/non)').lower()
    else:
        if q_d1 == 'oui':
            print('Avant tout sachez que le décodage soustrait le nombre donné (exemple: si nombre = 3'
                  ' alors erqmrxu devient bonjour.')
            print('Donc si vous voulez que le décodage additionne il vous suufit de faire 26 - votre nombre.')
            text = input('Entrer le texte à déchiffrer').lower()
            question2 = input('Connaissez vous le nombre permettant le décodage?'
                              ' Veuillez répondre par oui ou par non.').lower()
            while question2 != 'oui' and question2 != 'non':
                print('Réponse non valide')
                question2 = input('Connaissez vous le nombre permettant le décodage? '
                                  'Veuillez répondre par oui ou par non.').lower()
            else:
                if question2 == 'oui':
                    number = int(input('Entrer le nombre.'))
                    number = number % 26
                    final_list_d = []
                    for letter in text:
                        if letter in alphabet:
                            immatriculation_number = 0
                            while letter != alphabet[immatriculation_number]:
                                immatriculation_number += 1
                            else:
                                final_number_d = immatriculation_number - number
                                final_list_d.append(alphabet[final_number_d])
                        else:
                            if letter == ' ':
                                final_list_d.append(' ')
                            elif letter == '.':
                                final_list_d.append('.')
                            elif letter == ':':
                                final_list_d.append(':')
                            elif letter == ';':
                                final_list_d.append(';')
                            elif letter == ',':
                                final_list_d.append(',')
                            elif letter == '?':
                                final_list_d.append('?')
                            elif letter == '!':
                                final_list_d.append('!')
                            elif letter == "'":
                                final_list_d.append("'")
                            elif letter == '"':
                                final_list_d.append('"')
                            elif letter == '*':
                                final_list_d.append('*')
                            elif letter == '1':
                                final_list_d.append('1')
                            elif letter == '2':
                                final_list_d.append('2')
                            elif letter == '3':
                                final_list_d.append('3')
                            elif letter == '4':
                                final_list_d.append('4')
                            elif letter == '5':
                                final_list_d.append('5')
                            elif letter == '6':
                                final_list_d.append('6')
                            elif letter == '7':
                                final_list_d.append('7')
                            elif letter == '8':
                                final_list_d.append('8')
                            elif letter == '9':
                                final_list_d.append('9')
                            elif letter == '0':
                                final_list_d.append('0')
                            elif letter == '%':
                                final_list_d.append('%')
                            elif letter == '/':
                                final_list_d.append('/')
                            elif letter == '+':
                                final_list_d.append('+')
                            elif letter == '-':
                                final_list_d.append('-')
                            elif letter == '=':
                                final_list_d.append('=')
                            elif letter == '_':
                                final_list_d.append('_')
                            elif letter == '(':
                                final_list_d.append('(')
                            elif letter == ')':
                                final_list_d.append(')')
                            elif letter == '@':
                                final_list_d.append('@')
                            elif letter == '#':
                                final_list_d.append('#')
                            elif letter == '$':
                                final_list_d.append('$')
                            elif letter == '°':
                                final_list_d.append('°')
                            elif letter == '£':
                                final_list_d.append('£')
                            elif letter == '<':
                                final_list_d.append('<')
                            elif letter == '>':
                                final_list_d.append('>')
                            elif letter == '&':
                                final_list_d.append('&')
                            elif letter == '€':
                                final_list_d.append('€')
                            elif letter == 'é':
                                final_list_d.append('e')
                            elif letter == 'è':
                                final_list_d.append('e')
                            elif letter == 'ê':
                                final_list_d.append('e')
                            elif letter == 'ë':
                                final_list_d.append('e')
                            elif letter == 'à':
                                final_list_d.append('a')
                            elif letter == 'ù':
                                final_list_d.append('u')
                            elif letter == 'ç':
                                final_list_d.append('c')
                            elif letter == 'ô':
                                final_list_d.append('o')
                            elif letter == 'ï':
                                final_list_d.append('i')
                            elif letter == 'î':
                                final_list_d.append('i')
                            else:
                                print('Nous ne pouvons traduire certains caractères dont celui-ci.')
                    final_sentence_d = ''.join(final_list_d)
                    print('Résultat du décriptage:')
                    print(final_sentence_d)
                elif question2 == 'non':
                    final_list_d = []
                    for x in range(26):
                        for letter in text:
                            if letter in alphabet:
                                immatriculation_number = 0
                                while letter != alphabet[immatriculation_number]:
                                    immatriculation_number += 1
                                else:
                                    final_number_d = (immatriculation_number + x) % 26
                                    final_list_d.append(alphabet[final_number_d])
                            else:
                                if letter == ' ':
                                    final_list_d.append(' ')
                                elif letter == '.':
                                    final_list_d.append('.')
                                elif letter == ':':
                                    final_list_d.append(':')
                                elif letter == ';':
                                    final_list_d.append(';')
                                elif letter == ',':
                                    final_list_d.append(',')
                                elif letter == '?':
                                    final_list_d.append('?')
                                elif letter == '!':
                                    final_list_d.append('!')
                                elif letter == "'":
                                    final_list_d.append("'")
                                elif letter == '"':
                                    final_list_d.append('"')
                                elif letter == '*':
                                    final_list_d.append('*')
                                elif letter == '1':
                                    final_list_d.append('1')
                                elif letter == '2':
                                    final_list_d.append('2')
                                elif letter == '3':
                                    final_list_d.append('3')
                                elif letter == '4':
                                    final_list_d.append('4')
                                elif letter == '5':
                                    final_list_d.append('5')
                                elif letter == '6':
                                    final_list_d.append('6')
                                elif letter == '7':
                                    final_list_d.append('7')
                                elif letter == '8':
                                    final_list_d.append('8')
                                elif letter == '9':
                                    final_list_d.append('9')
                                elif letter == '0':
                                    final_list_d.append('0')
                                elif letter == '%':
                                    final_list_d.append('%')
                                elif letter == '/':
                                    final_list_d.append('/')
                                elif letter == '+':
                                    final_list_d.append('+')
                                elif letter == '-':
                                    final_list_d.append('-')
                                elif letter == '=':
                                    final_list_d.append('=')
                                elif letter == '_':
                                    final_list_d.append('_')
                                elif letter == '(':
                                    final_list_d.append('(')
                                elif letter == ')':
                                    final_list_d.append(')')
                                elif letter == '@':
                                    final_list_d.append('@')
                                elif letter == '#':
                                    final_list_d.append('#')
                                elif letter == '$':
                                    final_list_d.append('$')
                                elif letter == '°':
                                    final_list_d.append('°')
                                elif letter == '£':
                                    final_list_d.append('£')
                                elif letter == '<':
                                    final_list_d.append('<')
                                elif letter == '>':
                                    final_list_d.append('>')
                                elif letter == '&':
                                    final_list_d.append('&')
                                elif letter == '€':
                                    final_list_d.append('€')
                                elif letter == 'é':
                                    final_list_d.append('e')
                                elif letter == 'è':
                                    final_list_d.append('e')
                                elif letter == 'ê':
                                    final_list_d.append('e')
                                elif letter == 'ë':
                                    final_list_d.append('e')
                                elif letter == 'à':
                                    final_list_d.append('a')
                                elif letter == 'ù':
                                    final_list_d.append('u')
                                elif letter == 'ç':
                                    final_list_d.append('c')
                                elif letter == 'ô':
                                    final_list_d.append('o')
                                elif letter == 'ï':
                                    final_list_d.append('i')
                                elif letter == 'î':
                                    final_list_d.append('i')
                                else:
                                    print('Nous ne pouvons traduire certains caractères dont celui-ci.')
                        final_list_d.append('§')
                    first_sentence_d = ''.join(final_list_d)
                    last_list_d = first_sentence_d.split('§')
                    print('Résultats du décodage:')
                    for a in range(26):
                        print(last_list_d[a])


def morse_trad():
    morse_trad_list = []
    q_m = input('Voulez-vous traduire un texte en morse? (oui/non)').lower()
    while q_m != 'oui' and q_m != 'non':
        print('Réponse non valide')
        q_m = input('Voulez-vous traduire un texte en morse? (oui/non)').lower()
    else:
        if q_m == 'oui':
            text_m = input('Entrer le texte en morse').lower()
            list_m2 = text_m.split(' ')
            for letter in list_m2:
                if letter in morse_alphabet:
                    verification_number = 0
                    while letter != morse_alphabet[verification_number]:
                        verification_number += 1
                    else:
                        morse_trad_list.append(alphabet[verification_number])
                else:
                    if letter == '/':
                        morse_trad_list.append(' ')
                    elif letter == '.----':
                        morse_trad_list.append('1')
                    elif letter == '..---':
                        morse_trad_list.append('2')
                    elif letter == '...--':
                        morse_trad_list.append('3')
                    elif letter == '....-':
                        morse_trad_list.append('4')
                    elif letter == '.....':
                        morse_trad_list.append('5')
                    elif letter == '-....':
                        morse_trad_list.append('6')
                    elif letter == '--...':
                        morse_trad_list.append('7')
                    elif letter == '---..':
                        morse_trad_list.append('8')
                    elif letter == '----.':
                        morse_trad_list.append('9')
                    elif letter == '-----':
                        morse_trad_list.append('0')
                    elif letter == '.-.-.-':
                        morse_trad_list.append('.')
                    elif letter == '--..--':
                        morse_trad_list.append(',')
                    elif letter == '..--..':
                        morse_trad_list.append('?')
                    elif letter == ".----.":
                        morse_trad_list.append("'")
                    elif letter == '-.-.--':
                        morse_trad_list.append('!')
                    elif letter == '-..-.':
                        morse_trad_list.append('/')
                    elif letter == '-.--.':
                        morse_trad_list.append('(')
                    elif letter == '-.--.-':
                        morse_trad_list.append(')')
                    elif letter == '.-...':
                        morse_trad_list.append('&')
                    elif letter == '---...':
                        morse_trad_list.append(':')
                    elif letter == '-.-.-.':
                        morse_trad_list.append(';')
                    elif letter == '.-.-.':
                        morse_trad_list.append('+')
                    elif letter == '-....-':
                        morse_trad_list.append('-')
                    elif letter == '-...-':
                        morse_trad_list.append('=')
                    elif letter == '..-.-':
                        morse_trad_list.append('_')
                    elif letter == '.-..-.':
                        morse_trad_list.append('"')
                    elif letter == '...-..-':
                        morse_trad_list.append('$')
                    elif letter == '.--.-.':
                        morse_trad_list.append('@')
                    elif letter == '.':
                        morse_trad_list.append('é')
                    elif letter == '.':
                        morse_trad_list.append('è')
                    elif letter == '.':
                        morse_trad_list.append('ê')
                    elif letter == '.':
                        morse_trad_list.append('ë')
                    elif letter == '.-':
                        morse_trad_list.append('à')
                    elif letter == '..-':
                        morse_trad_list.append('ù')
                    elif letter == '-.-.':
                        morse_trad_list.append('ç')
                    elif letter == '---':
                        morse_trad_list.append('ô')
                    elif letter == '..':
                        morse_trad_list.append('ï')
                    elif letter == '..':
                        morse_trad_list.append('î')
                    else:
                        print(f'error: {letter}')
            sentence_trad = ''.join(morse_trad_list)
            print(f'Le texte en morse est "{sentence_trad}"')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
morse_alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..',
                  '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
                  '-.--', '--..']
question1 = input('Souhaitez vous déchiffer ou crypter un texte?'
                  ' Veuillez répondre "d" pour déchifrer ou "c" pour crypter.').lower()
while question1 != 'c' and question1 != 'd':
    print('Réponse non valide')
    question1 = input('Souhaitez vous déchiffer ou crypter un texte?'
                      ' Veuillez répondre "d" pour déchifrer ou "c" pour crypter.').lower()
else:
    if question1 == 'c':
        print(cryptage())
    elif question1 == 'd':
        print(decryptage())