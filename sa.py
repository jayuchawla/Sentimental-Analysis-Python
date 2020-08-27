
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(s):
    st=""
    c=0
    l = s.split(" ")
    for i in l:
        if i[0] in punctuation_chars:
            st = i[1:]
        elif i[-1] in punctuation_chars:
            st = i[:len(i)-1]
        else:
            st = i
        if st.lower() in negative_words:
            c+=1
    return c

def get_pos(s):
    st=""
    c=0
    l = s.split(" ")
    for i in l:
        if i[0] in punctuation_chars:
            st = i[1:]
        elif i[-1] in punctuation_chars:
            st = i[:len(i)-1]
        else:
            st = i
        if st.lower() in positive_words:
            c+=1
    return c

def strip_punctuation(s):
    st = ""
    for i in s:
        if i not in punctuation_chars:
            st+=i
    return st


i = 0
header = []
num_retweets = []
num_replies = []
pos_score = []
neg_score = []
net_score = []

header.append("Number of Retweets")
header.append("Number of Replies")
header.append("Positive Score")
header.append("Negative Score")
header.append("Net Score")

with open("project_twitter_data.csv","r") as f:
    for row in f:
        l = row.split(",")
        if i == 0:
            i+=1
            continue
        
        num_retweets.append(int(l[1]))
        num_replies.append(int(l[2][0]))
        ps = get_pos(l[0])
        ns = get_neg(l[0])
        pos_score.append(ps)
        neg_score.append(ns)
        net_score.append(ps-ns)
    #print(num_retweets)
    #print(num_replies)
    #print(pos_score)
    #print(neg_score)
    #print(net_score)

with open("resulting_data.csv","w") as f:
    for i in range(len(header)):
        f.write(header[i])
        if i < len(header)-1:
            f.write(", ")
    f.write("\n")
    for i in range(len(net_score)):
        f.write(str(num_retweets[i])+", ")
        f.write(str(num_replies[i])+", ")
        f.write(str(pos_score[i])+", ")
        f.write(str(neg_score[i])+", ")
        f.write(str(net_score[i]))
        f.write("\n")

with open("resulting_data.csv","r") as f:
    for row in f:
        print(row)
"""
Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score
3, 0, 0, 0, 0
1, 0, 2, 2, 0
1, 2, 1, 0, 1
3, 1, 1, 0, 1
6, 0, 2, 0, 2
9, 5, 2, 0, 2
19, 0, 1, 0, 1
0, 0, 0, 3, -3
0, 0, 0, 2, -2
82, 2, 4, 0, 4
0, 0, 0, 1, -1
0, 0, 1, 0, 1
47, 0, 2, 0, 2
2, 1, 1, 0, 1
0, 2, 1, 0, 1
0, 0, 2, 1, 1
4, 6, 3, 0, 3
19, 0, 3, 1, 2
0, 0, 1, 1, 0

"""