#------------------------------------------------String Methods-----------------------------------------------#
# Distilling a text
import re


# Counting wood.

text1 = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a Mr. Smith could chuck wood\n\r\t."""

def wood_counter(text):
    count = 0
    text = text.replace("?", "").replace(".","")
    # print(text)
    l = text.lower().strip().split()
    # print(l)

    for word in l:
        if word == "wood":
            count +=1
    print(count)

wood_counter(text1)

print("\n")


text = """The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. 
Junk MTV quiz graced by fox whelps. [Never gonna ] Bawds jog, flick quartz, vex nymphs. 
[give you up\n] Waltz, bad nymph, for quick jigs vex! Fox nymphs grab quick-jived waltz. 
Brick quiz whangs jumpy veldt fox. [Never ] Bright vixens jump; [gonna let ] dozy fowl 
quack. Quick wafting zephyrs vex bold Jim. Quick zephyrs blow, vexing daft Jim. Charged 
[you down\n] fop blew my junk TV quiz. How quickly daft jumping zebras vex. Two driven 
jocks help fax my big quiz. Quick, Baz, get my woven flax jodhpurs! "Now fax quiz Jack!" 
my brave ghost pled. [Never ] Five quacking zephyrs jolt my wax bed. [gonna ] Flummoxed 
by job, kvetching W. zaps Iraq. Cozy sphinx waves quart jug of bad milk. [run around ] 
A very bad quack might jinx zippy fowls. Few quips galvanized the mock jury box. Quick 
brown dogs jump over the lazy fox. The jay, pig, fox, zebra, and my wolves quack! 
[and desert you] Blowzy red vixens fight for a quick jump. Joaquin Phoenix was gazed 
by MTV for luck. A wizard’s job is to vex chumps quickly in fog. Watch "Jeopardy!", 
Alex Trebek's fun TV quiz game."""


clean_text = text.replace("\n", " ")
regex = re.compile(".*?\[(.*?)\]")
result = re.findall(regex, clean_text)
clean_result = "".join(result).split()
print(clean_result[0] + " " + clean_result[1] + " " + clean_result[2] + " " + clean_result[3] + " " + clean_result[4])
print(clean_result[5] + " " + clean_result[6] + " " + clean_result[7] + " " + clean_result[8] + " " + clean_result[9])
print(clean_result[10] + " " + clean_result[11] + " " + clean_result[12] + " " + clean_result[13] +
      " " + clean_result[14] + " " + clean_result[15])
print("\n")

# ROTR-13
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"*2
print(letters[:26])
count = 0
# while count < 52:
for i in range(len(letters)):
    if i >= 13:
        if i <= 38:
            # print(i)
            print(letters[i], end="")



print("\n")
# strip() removes spaces in front and ending of a string
s = "    And now for something completely different\n   "
print("["+s+"]")
s = s.strip()
print("["+s+"]")

# upper() and lower() cases convert to all capital and small letters respectively
s = "The Meaning of Life"
print(s)
print(s.upper())
print(s.lower())

# find() returns the index of a first letter or word been searched if not letter or word
# if no match it returns -1 or lower index of staring letter or word
s = "Humpty Dumpty sat on the wall"
print(s.find("sat"))
print(s.find("t"))
print(s.find("t", 12))
print(s.find("z"))
print(s.find(" "))
print("\n")

# replace() replaces the position of a substring with a new string. Note string is immutable
s = " Humpty Dumpty sat on the wall "
new_s = s.replace('sat on', 'fell off')
print(new_s)
print(s)
print("\n")

# split() seperate string with a character indicated by the user, if no character is indidcated it seperate with wite space
s = 'Humpty Dumpty sat on the wall'
wordlist = s.split()
for i in wordlist:
    print(i, end=" ")
print("\n")
print(wordlist)
print("\n")

csv = "2016,September,28,Data Processing,Tilburg University,Tilburg"
values = csv.split(',')
for value in values:
    print(value)

print("")
print(values)
print (values[1][0])

# join() joins list of words together seperated by a specific seperator
s = "Humpty;Dumpty;sat;on;the;wall"
print (s)
wordlist = s.split(';')
print (wordlist)
s = " ".join(wordlist)
print(s)

mess_str = "geeksforgeeksjhkjdshdsf"

# Iterate over the string
for each_let in mess_str:
    print(each_let, end=" ")
print("\n")


# Printing Indices and it corresponding  vowels
def index_vowels(text):
    for indix in range(len(text)):
        if text[indix].lower() in "aeiou":
            print(indix, ":", text[indix])


index_vowels(input("Please enter any word: "))
print("\n")


# Comparing two string and printing vowels common in the them at the same indix
s1 = "The Holy Grail"
s2 = "Life of Brian"


def similar_char(text1, text2):
    for indix in range(len(text2)):
        if text1[indix] in text2[indix]:
            print(text1[indix], "in position", indix)
    return ""


print(similar_char(s1, s2))


# String cleaning function
def clean_string(string):
    clean_str = ""
    for ch in string:
        if ch >= "a" and ch <= "z":
            clean_str += ch

        else:
            clean_str += " "
    print(clean_str)


clean_string(input("Please enter sentence to be cleaned: "))

print("\n")


#  Slicing of Strings
reduce_str = "Ayuba"
print(reduce_str[::1])  # Runs from zero indix to the end with step of one
print(reduce_str[::2])  # Runs from zero indix to the end with step of two
print(reduce_str[:4:1]) #Runs from zero indix to with step of one at each and every iterating but ends(3 letter)
print(reduce_str[1:5:2]) # Runs from one indix to the end with step of two at each and every iterating
print(reduce_str[::-1]) # Runs from last indix to the beginning with step of one (backwards slicing)
print(reduce_str[:-3:-1]) # Runs from last indix to the third indix with step of one (backwards slicing)
print(reduce_str[-2:-5:-1]) # Runs from last indix to the beginning with step of one (backwards slicing)
print(reduce_str[:-6:-1]) # Runs from last indix to the beginning with step of one (backwards slicing)