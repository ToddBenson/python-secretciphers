import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    myKey = 10
    myMode = 'decrypt'
    
    if myMode == 'encrypt':
        inputFilename = 'frankenstien.txt'
        outputFilename = 'frankenstien.encrypted.txt'

    if myMode == 'decrypt':
        inputFilename = 'frankenstien.encrypted.txt'
        outputFilename = 'frankenstien.decrypted.txt'
        

    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    if os.path.exists(inputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Quit)?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
                  sys.exit()
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()


    print('%sing...' % (myMode.title()))

    startTime = time.time()
    if myMode == 'encrypt':
          translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
          translated = transpositionDecrypt.decryptMessage(myKey, content)

    
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))
        

if __name__ == '__main__':
    main()              
