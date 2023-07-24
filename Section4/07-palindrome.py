def is_palindrome(text):
    inverse_Text = text[::-1]
    if(text == inverse_Text):
        print("The word is palindrome")
    else:
        print("The word is not palindrome")  

message = "ReCoNocer"
message = message.lower()
message = message.replace(" ","")
is_palindrome(message)