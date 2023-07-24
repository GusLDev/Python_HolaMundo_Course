def no_space(text):
    new_text = ""
    for char in text:
            if char != " ":
                new_text += char
    return new_text

def reverse(text):
    inverse_text = ""
    for char in text:
        inverse_text = char + inverse_text      
    return inverse_text

def is_palindrome(text):
    text = no_space(text)
    inverse_text = reverse(text)
    return text.lower() == inverse_text.lower()

print("AMO La Paloma",is_palindrome("AMO La Paloma"))

print("Hola Mundo",is_palindrome("Hola Mundo"))