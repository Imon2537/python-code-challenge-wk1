# it returns the number of vowels
def totalVowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

count = totalVowels("randervous")
print(count)
