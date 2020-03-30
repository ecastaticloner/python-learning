def smilyconverter(message):
    words = message.split(" ")
    emoji = {
        ":)" : "😀" ,
        ":(" : "😞"
    }
    output = ""
    for word in words :
        output += emoji.get(word,word)+" "
    return output


message = input(" Enter the message")
print(smilyconverter(message))
