## problem: ## If the numbers 1 to 5 are written out in word"s": one, two, three, four, five,then there
## are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the numbers from 1 to 1000
## (one thousand) inclusive were written out in words, how many letters would be used?

## NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
## contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of
## and when writing out numbers is in compliance with British usage.

## solution: import numpy as np
number_to_word_map = {
    "1": "one","2": "two","3": "three","4": "four","5": "five","6": "six","7": "seven","8": "eight","9": "nine","10": "ten",
    "11": "eleven","12": "twelve","13": "thirteen","14": "fourteen","15": "fifteen","16": "sixteen","17": "seventeen",
    "18": "eighteen","19": "nineteen","20": "twenty", "30": "thirty", "40": "forty","50": "fifty","60": "sixty","70": "seventy",
    "80": "eighty","90": "ninety", "100": "onehundred", "200": "twohundred", "300": "threehundred", "400": "fourhundred", "500": "fivehundred",
    "600": "sixhundred", "700": "sevenhundred", "800": "eighthundred", "900": "ninehundred", "1000": "onethousand"
}

two_initial_to_word_map = {
    "2": "twenty","3": "thirty","4": "forty","5": "fifty","6": "sixty","7": "seventy","8": "eighty","9": "ninety"
}

three_initial_to_word_map = {
    "1": "onehundredand", "2": "twohundredand", "3": "threehundredand", "4": "fourhundredand", "5": "fivehundredand",
    "6": "sixhundredand", "7": "sevenhundredand", "8": "eighthundredand", "9": "ninehundredand"
}

def convert_to_words(number):
    number = str(int(number))
    words = number_to_word_map.get(number)
    if words:
        return words
    else:
        if(len(number) == 2):
            words = two_initial_to_word_map.get(number[:1]) + convert_to_words(number[1:])
        elif(len(number) == 3):
            words = three_initial_to_word_map.get(number[:1]) + convert_to_words(number[1:])
        else:
            print("not supported", number)
        return words

def letters_count(limit):
    count = 0
    for i in range(1,limit+1):
        count += len(convert_to_words(i))
    return count

assert convert_to_words(2)=="two"
assert convert_to_words(13)=="thirteen"
assert convert_to_words(21)=="twentyone"
assert convert_to_words(99)=="ninetynine"
assert convert_to_words(300)=="threehundred"
assert convert_to_words(334)=="threehundredandthirtyfour"
assert convert_to_words(999)=="ninehundredandninetynine"

assert letters_count(5)==19
assert letters_count(99) == 854
assert letters_count(19) == 106
assert letters_count(1000) == 21124
assert letters_count(1000) == 21124

print("all test passed")
