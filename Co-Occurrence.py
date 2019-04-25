import csv

def map(row, top_words, list) : 
    word_list = row.split()
    for top_word in top_words:
        # for word in row :
        if top_word in word_list:
            for word in word_list:
                if top_word != word: 
                    list.append(((top_word, word), [1]))
                    # print(((top_word, word), [1]))
            

def reducer (list, newList) :
    for pair in list : 
        counter = 0
        for pablosaused in list:
            if pablosaused[0] == pair[0]:
                counter +=1
        newList.append((pair[0],counter)) 
        # print(pair[0] + "  " + pair[1])

def write_to_nyttxt (list) : 
    file = open("nytOccur.txt", "w")
    for pair in list : 
       file.write(str(pair[0]) + "  " + str(pair[1]) + "\n")
    file.close()

def write_to_tweettxt (list) : 
    file = open("tweetOccur.txt", "w")
    for pair in list : 
        file.write(str(pair[0]) + "  " + str(pair[1]) + "\n")
    file.close()

def write_to_cctxt (list) : 
    file = open("ccOccur.txt", "w")
    for pair in list : 
        file.write(str(pair[0]) + "  " + str(pair[1]) + "\n")
    file.close()
                            
nyt_top_words = ["said", "team", "game", "player","play","one", "year", "will", "like", "new"]
nyt_occurence_list = []
nyt_word_occurrence_list = []

twitter_top_words = ["sport", "game", "team", "win", "get", "like", "one", "final", "just", "play"] 
twitter_occurence_list = []
twitter_word_occurrence_list = []

cc_top_words = ["sport", "team", "soccer", "pm", "news", "us", "game", "football", "new", "home"] 
cc_occurence_list = []
cc_word_occurrence_list = []


nytfile = open("nytscrub.txt")
counter = 0
for row in nytfile: 
    if counter != 3 :
        map(row, nyt_top_words, nyt_occurence_list)
        reducer(nyt_occurence_list, nyt_word_occurrence_list)
        counter = counter + 1
write_to_nyttxt(nyt_word_occurrence_list)

twfile = open("tweetscrub.txt")
for row in nytfile: 
    map(row, twitter_top_words, twitter_occurence_list)
    reducer(twitter_occurence_list, twitter_word_occurrence_list)
write_to_tweettxt(twitter_word_occurrence_list)


ccfile = open("ccscrub.txt")
for row in nytfile: 
    map(row, cc_top_words, cc_occurence_list)
    reducer(cc_occurence_list, cc_word_occurrence_list)
write_to_cctxt(cc_word_occurrence_list)