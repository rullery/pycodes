import pyperclip

def this_or_that(question):
    while "the answer is invalid":
        reply = str(input(question+' (e/d): ')).lower().strip()
        if reply[0] == 'e':
            return True
        if reply[0] == 'd':
            return False


mode = this_or_that('Encrypt or Decrypt?')
print('Key to use (integer)')
key = int(input())
print('Message to operate on:')
message = input()
translated = ''
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        if mode:
            translatedIndex = symbolIndex + key
        else:
            translatedIndex = symbolIndex - key

        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol

print(translated)

