import json

json_file = open('dataset.txt', 'r', encoding='utf-8')
dataSet = json.load(json_file)
json_file.close()

print(dataSet["intents"][0]['patterns'])


def matchWord(w1, pw):
    str1 = w1.lower()
    str2 = pw.lower()
    con = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            con = con + 1
    return (con / len(str2)) * 100

print(matchWord('Hello','Hello'))

def matchSectence(s1, arrOfPatt):
    senArr = s1.split()
    for pattern in arrOfPatt:
        patArr = pattern.split()
        for i in range(100):

