"""
I highly recommend to use the terminal to see the magic.

THE IDEA:
    make an encryption system that convert a -> z , b -> y.
    the opposite of alphabet.
    use it to snd code messages :),
    make an encryptor and decryptor too.
    MAKE IT COOL TO WATCH (see it using terminal) :).

    example:
        input message  cat

        convert message -> encrypt(message)

        c=x a =z t=g
        cat ==> xzg

        output encrypted message -> xzg
"""
import time

TIME_DELAY = 0.01
alpha = {
    ' ': ' ',
    'a': 'z',
    'b': 'y',
    'c': 'x',
    'd': 'w',
    'e': 'v',
    'f': 'u',
    'g': 't',
    'h': 's',
    'i': 'r',
    'j': 'q',
    'k': 'p',
    'l': 'o',
    'm': 'n',
    'n': 'm',
    'o': 'l',
    'p': 'k',
    'q': 'j',
    'r': 'i',
    's': 'h',
    't': 'g',
    'u': 'f',
    'v': 'e',
    'w': 'd',
    'x': 'c',
    'y': 'b',
    'z': 'a',
    'A': 'Z',
    'B': 'Y',
    'C': 'X',
    'D': 'W',
    'E': 'V',
    'F': 'U',
    'G': 'T',
    'H': 'S',
    'I': 'R',
    'J': 'Q',
    'K': 'P',
    'L': 'O',
    'M': 'N',
    'N': 'M',
    'O': 'L',
    'P': 'K',
    'Q': 'J',
    'R': 'I',
    'S': 'H',
    'T': 'G',
    'U': 'F',
    'V': 'E',
    'W': 'D',
    'X': 'C',
    'Y': 'B',
    'Z': 'A',
    '0': '9',
    '1': '8',
    '2': '7',
    '3': '6',
    '4': '5',
    '5': '4',
    '6': '3',
    '7': '2',
    '8': '1',
    '9': '0',

}


def encrypt(message: str) -> None:
    new_message = ''
    count = 0

    while True:
        if len(message) == len(new_message):
            print(new_message)
            break
        elif message[count] == '':
            new_message += ''
            count += 1
        else:
            for i, x in alpha.items():
                if len(message) == len(new_message):
                    pass
                else:
                    print(new_message + x, end='\r')
                    time.sleep(TIME_DELAY)
                    if i == message[count]:
                        new_message += x
                        count += 1
                    elif message[count] not in alpha.keys():
                        new_message += message[count]
                        count += 1


if __name__ == '__main__':
    print('Please enter a message to ->')
    msg = input("encrypt/decrypt\n :")
    if msg != '':
        encrypt(msg)
        input('press any key to continue ->')
    else:
        print("Invalid")
