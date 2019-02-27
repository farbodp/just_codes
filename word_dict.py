my_file = open('alice.txt', mode='r')
lines = my_file.readlines()

word_dict = {}
for line in lines:
    words = line.split()
    for word in words:
        word = word.lower()
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1

for key in sorted(word_dict.keys()):
    print(key +': '+ str(word_dict[key]))

my_file.close()
