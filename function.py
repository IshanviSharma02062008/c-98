def countWordsFromFile():
    f=open("C:/Users/my pc/OneDrive/Documents/python/C-98/test.txt")
    fileLines=f.readlines()
    #fileName= input( "Enter the file name")
    noOfWords=0
    #file=open(fileName,'r')
    for line in fileLines:
        words= line.split()    
        noOfWords=noOfWords+len(words)
    print("No Of Words:")   
    print(noOfWords)  

countWordsFromFile()    