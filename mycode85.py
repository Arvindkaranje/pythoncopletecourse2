# 114
# practice problem 6 solution

# 115
# problem 7 question
# search engine

"""you are given few sentences as a list(python list of sentence). take a query string as an user input from the user.
you have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after
converting every word in the query and the sentences to lowercase. most relevant sentences is the one with the maximum
number of matching words with the query."""

# sentences =["this is good,"python is so good","python is not python snake"]

# input
# please input your query string
# "python is"

# output
# 3 related results found
# python is not python snake
# python is so good
# this is good

def matchingwords(sentense1,sentense2):
    words1=sentense1.split()
    words2=sentense2.split()
    score=0
    for word1 in words1:
        for word2 in words2:
            if word1.lower==word2.lower:
                score +=1
    return score


if __name__=="__main__":
    # sentences which are given to search the query and process search engine
    sentences = ["this is good", "python is good", "python is not python snake"]
    query=(input("Enter the query here\n"))
    scores=[matchingwords(query,sentense) for sentense in sentences]
    # print(scores)
    sortedsentscore=[sentscore for sentscore in sorted(zip(scores,sentences),reverse=True)if sentscore[0]!=0]

    print(f"{len(sortedsentscore)} results found")
    for score,item in sortedsentscore:
        print(f"\"{item}\" : with a score of {score}")





