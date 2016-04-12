import detectEnglish, transpositionDecrypt

def main():
    inputFilename = 'frankenstien.encrypted.txt'
    fileObj = open(inputFilename)
    message = fileObj.read()
    fileObj.close()
    hackedMessage = hackTransposition(message)

    if hackedMessage == None:
        print('Failed to hack encryption')

def hackTransposition(message):
    print('Hacking...')

    print('(press Ctrl-C or Ctrl-D to quit at any time.)')

    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))
        decryptedText = transpositionDecrypt.decryptMessage(key, message)

     
        if detectEnglish.isEnglish(decryptedText, 10, 10):
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D for done, or just press Enter to continue hacking')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

if __name__ == '__main__':
    main()

