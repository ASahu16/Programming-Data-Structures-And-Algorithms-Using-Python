# Write a Python function maxaverage(l) that takes a list of pairs of the form (name,score) as argument, 
# where name is a string and score is an integer. 
# Each pair is to be interpreted as the score of the named player. 
# For instance, an input of the form [('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)] 
# represents two scores of 73 and 7 for Kohli, two scores of 33 and 90 for Ashwin and one score of 122 for Pujara. 
# Your function should compute the players who have the highest average score 
# (average = total across all scores for that player divided by number of entries) 
# and return the list of names of these players as a list, sorted in alphabetical order. 
# If there is a single player, the list will contain a single name.

# For instance, maxaverage([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)]) 
# should return ['Pujara'] because the average score 
# of Kolhi is 40 (80 divided by 2), 
# of Ashwin is 61.5 (123 divided by 2) and 
# of Pujara is 122 (122 divided by 1), 
# of which 122 is the highest.

def maxaverage(l):
    series_score = {}
    for i in l:
        name, score = i
        try:
            total_score, total_match = series_score[name]
            series_score[name] = (total_score+score, total_match+1)
        except:
            series_score[name] = (score, 1)
    max= -1
    for key in series_score:
        total_score, total_match = series_score[key]
        ave = total_score/total_match
        if(max < ave):
            max = ave
    l = []
    for key in series_score:
        total_score, total_match = series_score[key]
        ave = total_score/total_match
        if(max == ave):
            l.append(key)
    l.sort()
    return l



print(maxaverage([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)]))
