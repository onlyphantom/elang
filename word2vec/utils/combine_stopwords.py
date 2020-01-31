import os
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

realpath = os.path.dirname(os.path.realpath(__file__))
stopwords_list_path = realpath + "/stopwords-list"
file_list = os.listdir(stopwords_list_path)

def generate_sastrawi_stopwords():
    # get Sastrawi stopwords as list
    factory = StopWordRemoverFactory()
    stopwords = factory.get_stop_words()

    # write to txt file
    with open(stopwords_list_path + '/sastrawi-stopwords.txt', 'w') as file:
        for word in stopwords:
            file.write(word + "\n")

def combine_stopwords_files(combined_filename = "stopwords-id.txt"):
    # combine all txt files
    combined_stopwords = []

    for filename in file_list:
        stopwords = open(stopwords_list_path + "/" + filename).read().splitlines()
        combined_stopwords.extend(stopwords)
        
        #print(filename, str(len(stopwords)))

    # remove duplicate and sort
    unique_stopwords = sorted(set(combined_stopwords))

    # write to new txt file
    with open(realpath + "/" + combined_filename, "w") as file:
        for word in unique_stopwords:
            file.write(word + "\n")

    #print("TOTAL", len(combined_stopwords))
    #print("UNIQUE", len(unique_stopwords))

generate_sastrawi_stopwords()
combine_stopwords_files()