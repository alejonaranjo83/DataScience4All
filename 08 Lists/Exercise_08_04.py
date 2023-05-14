# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words
# using the split() method. The program should build
# a list of words. For each word on each line check
# to see if the word is already in the list and if not
# append it to the list. When the program completes,
# sort and print the resulting words in alphabetical order.
# You can download the sample data at
# http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for renglon in fh:
    #con el siguiente SPLIT se genera una lista por
    #cada renglon (4 en total)
    renglon = renglon.split()
    #se genera una nueva iteración para extraer las palabras
    #de cada renglon
    for palabra in renglon:
        #se genera una lista con las diferentes palabras (APPEND)
        #siempre y cuando (IF) esa palabra no se haya
        #introducido previamente en la lista (NOT IN)
        if (palabra not in lst):
            lst.append(palabra)
        #en caso de q sí esté, se la debe saltar (CONTINUE)
        else:
            continue
        #al interior de esa lista, organice las palabras
        #alfabéticamente (SORT... de menor a mayor)
        lst.sort()
print(lst)




# Desired answer:
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
# 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
# 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
