def Word_Replacement_Program():
    
    print(" ")
    print(" ")
    print("--------Welcome To The Word Replacer---------")
    print(" ")
    
    User_Message = input("Enter The Message: ")
    # Message = "This is a word replacement program."
    
    word_to_be_replaced = input("Enter The Word That You Want To Replace: ")
    
    replacement_word = input("Enter The Word That You Want To Replace in Place Of Original Word: ")
    
    # print(Message.replace(word_to_be_replaced, replacement_word))
    print(User_Message.replace(word_to_be_replaced, replacement_word))
    
Word_Replacement_Program()