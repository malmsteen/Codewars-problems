MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
              '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', }


def decode_bits(bits):

    period = 0
    while True:
        if bits[::1] == bits[period::1]:
            period += 1
        else:
            period += 1
            break

    resampled_bits = bits.replace('1'*period*3, '-').replace('0'*period,
                                                             ' ').replace('1' * period, '.').replace('0', '')
    # print(period)
    # print(resampled_bits)
    return resampled_bits


#     return bits.replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')


def decode_morse(morseCode):
    # morseCode.replace('.', MORSE_CODE['.']).replace(
    #     '-', MORSE_CODE['-']).replace(' ', '')
    decoded = []
    for word in morseCode.split(' '*7):
        decoded.append(''.join([MORSE_CODE[ch.replace(' ', '')]
                                for ch in word.split(' '*3)]))

    return ' '.join(decoded).strip()
    # ToDo: Accept dots, dashes and spaces, return human-readable message
#     return morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')


bits = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
morse = decode_bits(bits)
print(decode_bits(bits))
print(decode_morse(morse))
