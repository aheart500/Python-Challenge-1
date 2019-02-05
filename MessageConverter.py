alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
message = 'map'
newMessage = []
for letter in message:
    if letter in alphabet:
        y =  alphabet.index(letter)
        if y==24:
            y = 0
            newMessage.append(alphabet[y])
        elif y== 25:
            y =1
            newMessage.append(alphabet[y])
        else:
            newMessage.append(alphabet[y+2])
    else:
        newMessage.append(letter)
theConvertedMessage = ''.join(newMessage)
print(theConvertedMessage)
