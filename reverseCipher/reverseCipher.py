# reverse cipher
# “https://www.nostarch.com/crackingcodes/ (BSD Licensed)”

print('input a mesasge:')
message = input()
translated = ''
i = len(message) - 1 
while i >= 0:
    translated = translated + message[i]
    i=i-1

print(translated)