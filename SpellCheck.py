import tqdm
from tqdm import tqdm

def remove_words(words):
    return [i for i in words if len(i) >= 6]

alphabeth = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","x","q","w"]

my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.replace('\n', ' ').split(" ")
my_file.close()
print(content_list)

dict_file = open("google-10000-english.txt", "r")
dictionary = dict_file.read()
dictionary_list = dictionary.replace('\n', ' ').split(" ")
dict_file.close()

reduced_dictionary = remove_words(dictionary_list)
print("number of words with more than 5 characters: %d" %(len(reduced_dictionary)))



def word_trial_set(i):
    augmented = ["list"]

    #print("------------------Input List------------------")
    #print(content_list)

    for j in range(1, len(content_list[i])):
        for k in range(len(alphabeth)):
            augmented += [content_list[i][:j] + alphabeth[k] + content_list[i][j:]]

    augmented.pop(0)
    #print("------------------Augmented part of Trial Set------------------")
    #print(augmented)
    diminished = ["list"]
    for j in range(len(list(content_list[i]))):
        a = list(content_list[i])
        a.pop(j)
        diminished += [''.join(a)]

    diminished.pop(0)
    #print("------------------Diminished part of Trial Set------------------")
    #print(diminished)
    #print(len(diminished))


    trial_set = augmented + diminished
    #print(len(trial_set))
    #print(trial_set)


    return trial_set

word_trial_set(1)


"""
import json

with open('augmented_file.txt', 'w') as filehandle:
    json.dump(augmented, filehandle)
"""

"""
import json

with open('diminished_file.txt', 'w') as filehandle:
    json.dump(diminished, filehandle)
"""

# This is the part that we traverse the dictionary and check if there appears any match or recommendation

for i in tqdm(range(len(reduced_dictionary))):
    for j in range(len(content_list)):
        if content_list[j] == reduced_dictionary[i]:
            print("%s --> OK" %(content_list[j]))
        else:
            for k in range(len(word_trial_set(j))):
                if word_trial_set(j)[k] == reduced_dictionary[i]:
                    print("%s --> %s" %(content_list[j],reduced_dictionary[i]))

