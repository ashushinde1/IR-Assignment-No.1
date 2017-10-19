import os
import codecs
import math
def get_total_words(filepath):
    total_words = []
    for root,dirs,files in os.walk(filepath):
        for name in files:
            [total_words.append(x.encode('ascii','replace')) for x in
             codecs.open(os.path.join(root, name),"r",encoding="utf-8-sig").read().split()]

    return total_words

def get_top_30(unique_word_set):
    dic = {}
    for i in unique_word_set:
        if i not in dic:
            dic[i] = 1
        elif i in dic:
            dic[i] += 1
    t = sorted(dic.items(), key=lambda x: -x[1])[:30]

    return t

def freq_tf(number_of_occurences, number_of_uniq_wrds):
        return number_of_occurences/number_of_uniq_wrds

def freq_Idf(total_files,number_of_files_for_word):
    return math.log(total_files/number_of_files_for_word)


def number_of_files_word_in(wordToSearch, filepath):
    fileCount =0
    for root, dirs, files in os.walk(filepath):
        for name in files:
                infile = open(filepath + "\\" + name, 'r')
                data = infile.read()
                words = data.split()
                if wordToSearch in words:
                    fileCount += 1

    return fileCount

if __name__ == '__main__':
    file_path = "C:\\Users\\meeta\\Desktop\\Transcripts"
    total_word_set = get_total_words(file_path)
    total_words = len(total_word_set)
    top_thirty_words = get_top_30(total_word_set)
    list = os.listdir(file_path)  # dir is your directory path
    number_files = len(list)

    for x in top_thirty_words:
        tf = freq_tf(x[1],total_words)
        number_of_files_for_word = number_of_files_word_in(x[0].decode("utf-8"), file_path)
        idf =freq_Idf(number_files, number_of_files_for_word)
        print("Total files: ", number_files, "Total Words: ", total_words)
        print("Word '", x[0].decode("utf-8"), "' Total Occurences ", x[1], "Number of file word found in: ",number_of_files_for_word, "TF ", tf, "Idf ", idf, "TF* Idf ", tf*idf, "Probability ", tf/total_words)

print("Average word tokens per document: ", total_words/number_files)