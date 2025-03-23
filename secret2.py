# Step 1: Ask if the user wants to encode a message
choice = input("Do you want to encode a message or receive one? (encode/receive): ").strip().lower()

if choice == "encode":
    message = input("Enter your message:\n")
    words = message.split()

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
    
    # Step 2: Ask if they want to decode their own message
    decode_choice = input("Do you want to decode the message? (yes/no): ").strip().lower()

    if decode_choice == "yes":
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
    else:
        print(f"You can send this encoded message{encoded_message} to someone!")

elif choice == "receive":
    received_message = input("Enter the encoded message you received:\n")

    de_words=received_message.split()
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
else:
    print("Invalid choice! Exiting.")
