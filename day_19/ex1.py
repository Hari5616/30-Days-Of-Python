with open("data/obama_speech.txt") as f:
    limes=f.read().splitlines()
    count_words=0
    for i in limes:
        words=i.split(" ")
        count_words+=len(words)
    #print("Number of lines is",len(limes))
    #print("No od words in txt is",count_words)


  #All are same thing that are in before ex but there i gave input here we read it thats the only difference       
