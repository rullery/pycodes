print('Enter message to brute force:')
message = input()
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


for key in range(len(SYMBOLS)):
    translated = ''
    for symbol in message:        
        symbolIndex = SYMBOLS.find(symbol)
        translatedIndex = symbolIndex - key

        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)

        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
            
        translated = translated + SYMBOLS[translatedIndex]
    print('Key #%s: %s' % (key, translated))