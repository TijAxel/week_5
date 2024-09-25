# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
print("problem set 1")
# a. Retrieve the 5th character.
tell='abracadabra'
print('part A')
print(tell[5])
# b. Retrieve the second to last character.
print('part B')
print(tell[-2])
# c. Find the first occurrence of the letter 'c'.
print('part C')
fin=(tell.find('c'))
print(fin)
 

print('Advanced Slicing:')
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alpha = 'abcdefghijklmnopqrstuvwxyz'

# a. Extract the letters 'hij'.
print('part A')
sig=(alpha.find('h'))
print(alpha[sig:10])
# b. Extract every second letter starting from 'a' to 'm'.
print("part B")
asf=(alpha.find('m'))
print(alpha[0:12:2])
# c. Reverse the entire string using slicing.
print('part C')
print(alpha[::-1])


# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.

print('problem set 2')
quote="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy "
print(quote[83:98])
print('part A')
info='Python is fun. Fun is good. Good is subjective. '
sub=(info.find('subjective.'))
print(info[sub:-1])
print('part B')
print(info[0::3])
print("part C")
print(info[::-1])


# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
print("problem set 3")
text1=("MAY THE FORCE BE WITH YOU")
print(text1.lower)
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.

motto1 = ("Make")
motto2 = ("haste")
motto3 = ("slowly")
print(motto1[3:])
print(motto2[2:])
print(motto3)

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
sentence=("Life is what happens when you are busy making other plans.")
print(sentence.replace("busy", "distracted"))
print(sentence.replace("plans", "mistakes"))

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
print("Problem Set 4")
print("iteration"*7)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
text="With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print(text.find("moonlight"))
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
my_string = "Supercalifragilisticexpialidocious"
count = len(my_string)
print("Total characters:", count)
# b. Count the number of times the letter 'i' appears in the same word/phrase.
text2 = "Supercalifragilisticexpialidocious"
print(text2.count("i"))
