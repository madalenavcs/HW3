from urllib.request import urlopen
#https://www.gutenberg.org/files/18220/18220-h/18220-h.htm
#url = "https://www.gutenberg.org/cache/epub/17515/pg17515.html"
local_name = "Reliquia.txt"


while True:
    livro = input("Choose between Reliquia or Cidade:")
    if livro == "Reliquia" or livro == "Cidade":
        print("Thanks! Now we will see what are the characteristics of this books' words")
        break
    else:
        print("That is not an option")

if livro == "Cidade":
    url = "https://www.gutenberg.org/files/18220/18220-h/18220-h.htm"
if livro == "Reliquia":
    url = "https://www.gutenberg.org/cache/epub/17515/pg17515.html"



def save_locally():
    with open(local_name, "w") as local_fp:
        with urlopen(url) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")                              #this refers to the type of font and removes paragraphs
                local_fp.write(line)
save_locally()

punctuation = ",;!.?-()"
def get_unique_words():
    """
    Get the dictionary of unique words and their frequency
    :return: dict
    """
    unique_words = {}
    with open(local_name) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            # get the words:
            for word in line.split():                                       #lo convierte en una lista de las palabras individuales
                unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words


unique_words = get_unique_words()
most_frequent = list(unique_words.values())                                 # values gives the "dfinition of the dic" which in this case is the number of times it appears
most_frequent.sort(reverse=True)

print(most_frequent)
for word_frequency in most_frequent[:10]:
    for unique_word, value in unique_words.items():                        #because this gives us word and its def separated by a , (unique_words.items)
        if word_frequency == value:
            print(f"common word '{unique_word}' appears {value} times")
            # change the value so we don't get it again if there are multiple words with the same frequency
            unique_words[unique_word] = -1
            break

a = len(unique_words)
print( "This book has", a , "different words")

all_words=list(unique_words.keys())

c=[]

for palavra in all_words:
    b=list(palavra)
    if len(b) >= 7:
        c.append(palavra)

print("This book has",len(c), " different words with more than 7 letters")

print("The book has", sum(unique_words.values()),"words in total")

proportion = len(c) * 100 / sum(unique_words.values())
print("This book has", round(proportion, 2) , "% of the words having more than 7 letters ")


#These two books are from a very famous Portuguese writer that I really like and wanted to compare which one would be more "complex"
#The book "Cidade" ("A Cidade e as Serras" is the official name) is in the a mandatory reading and the other one is less known but
# I personally liked it more. The complexity is similar which makes sense since the author is the same. The mandatory reading one has
# a lower complex words per total of words percentage
