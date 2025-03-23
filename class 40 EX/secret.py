# Taking Input:
message = input("Enter your message:\n")
words = message.split()

# Coding the message
import random
random_chars = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(3))
encoded_words=[]
for word in words:
    if len(word) >= 3:  
        word = word[1:] + word[0]
        random_chars = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(3))
        word= random_chars+word+random_chars
        # print(word)
    if len(word)<=2:
        word = word[::-1] 
    encoded_words.append(word)
encoded_message=" ".join(encoded_words)
print(encoded_message)
print("Message is EnCoded succesfullly!\n")


# Decoding Code:
de_words=encoded_message.split()
decoded_words=[]
for de_word in de_words:
    if len(de_word)>=9:
        de_word= de_word[3:-3]
        de_word=de_word[-1]+de_word[:-1]
    else:
        de_word=de_word[::-1]
    decoded_words.append(de_word)
de_message=" ".join(decoded_words)

print(de_message)
print("Message decode succesfully")