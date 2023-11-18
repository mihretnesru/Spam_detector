import string
from string import digits
import re

# load lines from file
def loadLines(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return lines

# parse lines into word list and count msgs
def parseLines(lines, keyword):
    pasredWords = []
    msgCount = 0
    for line in lines:
        if keyword in line:
            msgCount += 1
            for word in line.replace(keyword, '') \
                            .translate(str.maketrans('', '', string.punctuation)) \
                            .translate(str.maketrans('', '', digits)) \
                            .split():
                pasredWords.append(word.lower())
    return pasredWords, msgCount

# create dict to count frequency    
def countFrequency(words):
    freq = {}
    for item in words:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
 
# function to get the probability for spam and ham
prob={}
def ham_probability(word):
    for key,value in word.items():
        if key in hamWordsFrequency:
            for w,count in word.items():
                prob[w]=count/hamMsgCount
     #print(prob)
    return prob
def spam_probability(word):
    for key, value in word.items():
        if key in spamWordsFrequency:
            for w, count in word.items():
                prob[w] = count / spamMsgCount
    #print(prob)
    return prob

#performing a computation on the porbabilities
def finalfunction(inputwords):
    spam_word_prob={}
    ham_word_prob = {}
    spam_prob_total = 1
    ham_prob_total= 1
    inputwords=inputwords.split()
    for word in inputwords:
        if word in spam_probability(spamWordsFrequency):
            spam_word_prob[word]=spam_probability(spamWordsFrequency)[word]
    for value in spam_word_prob.values():
        spam_prob_total*=value
    spam_prob_total*=spam_prob

    for word in inputwords:
        if word in ham_probability(hamWordsFrequency):
            ham_word_prob[word]=ham_probability(hamWordsFrequency)[word]
    for value in ham_word_prob.values():
        ham_prob_total *= value
    ham_prob_total *= ham_prob

    print(f"spam probabilty: {spam_word_prob}")
    print(f"ham probabilty:{ham_word_prob}")

    if spam_prob_total>ham_prob_total: #checking if the total prob of scam is greater than ham
        print("Your message is a Spam!")
    else:
        print("Your message is a Ham")


if __name__ == "__main__":

    rawLines = loadLines("SMSSpamCollection") #reading the txt file

    spam = parseLines(rawLines, "spam\t")   #parsing the line
    spamWords = spam[0]
    spamMsgCount = spam[1]

    spamWordsFrequency = countFrequency(spamWords)  #counting the frequencies

    ham = parseLines(rawLines, "ham\t")
    hamWords = ham[0]
    hamMsgCount = ham[1]
    hamWordsFrequency = countFrequency(hamWords)

    spam_prob= spamMsgCount/(spamMsgCount+hamMsgCount) # prob of spam message
    ham_prob = hamMsgCount / (spamMsgCount + hamMsgCount) # prob of ham message

    user_input = input("Welcome to the Scam detecting tool \n write the message\n")  #taking input from user
    user_input=user_input.lower()  #change to lower case
    special_chars_pattern = r'[.,!?":;]'
    user_input=re.sub(special_chars_pattern, ' ', user_input)
    finalfunction(user_input)





