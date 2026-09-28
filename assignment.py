# You can remove 'pass' if you written code in the function

# Exercise 1
def is_valid_email(text):
    r=0
    c=0
    for char in text:
        if '@' in char:
            r=r+1
        if '.' in char:
            c=c+1
    if r>=1 and c>=1:
        return "Valid"
    else:
        return "Invalid"
# Exercise 2
def remove_vowels(text):
    v="aioeuAIOUE"
    f=""
    for char in text:
        if char not in v:
         f=f+char
    return f
pass
# Exercise 3
def get_initials(text):
    text=text.split()
    i=""
    for word in text:
     f=text[0].upper()
     i=i+f+'.'
     return i
pass
# Exercise 4
def extract_year(text):
    v = "1234567890"
    f = ""
    for char in text:
        if char not in v:
            f = f + char
    return f
pass
# Exercise 5
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
    pass
