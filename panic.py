phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for letter in range(len(plist) - 1, 2, -1):
    plist.pop(letter)
plist.remove('D')
plist.extend(' tap')

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
