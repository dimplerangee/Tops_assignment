# ask usr to enter a letter
letter = input("enter a single letter:")

# convert the letter to lower case 
letter = letter.lower()

#check if letter to is a vowel
if letter in ['a','e','i','o','u']:
    print(letter,"is a vowel.")
else:
    print(letter,"is not a vowel")
