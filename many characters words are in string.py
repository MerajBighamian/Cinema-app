#how many characters words are in string
string="hello im meraj bighamian im a programmer fullstack"
def n_word_in_str(str1,n):
    number_of_character=0
    words=str1.split()
    for this_word in words:
        if len(this_word)==n:
            number_of_character+=1
    return number_of_character
for n in range(1,len(string)):
    n_words=n_word_in_str(string,n)
    print("number of",n,"words is ",n_words)