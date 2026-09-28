# You can remove 'pass' if you written code in the function

# Exercise 1
def is_valid_email(text):
    r = 0
    c = 0
    for char in text:
        if '@' in char:
            r = r + 1
        if '.' in char:
            c = c + 1
    if r >= 1 and c >= 1:
        return "Valid"
    else:
        return "Invalid"
# Exercise 2
def remove_vowels(text):
    v = "aioeuAIOUE"
    f = ""
    for char in text:
        if char not in v:
            f = f + char
    return f
# Exercise 3
def get_initials(text):
    words = text.split()
    i = ""
    for word in words:
        i = i + word[0].upper() + '.'
    return i
# Exercise 4
def extract_year(text):
    words = text.split()
    for word in words:
        digits = ""
        for char in word:
            if char in "0123456789":
                digits = digits + char
        if len(digits) == 4:
            return digits
    return False
# Exercise 5
def is_palindrome(text):
    cleaned = ""
    for char in text.lower():
        if char.isalnum():
            cleaned = cleaned + char
    return cleaned == cleaned[::-1]
