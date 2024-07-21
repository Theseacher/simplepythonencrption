    #a list of all the letters in the alphabet
k = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    #amount of words to go back
index = 3
    #function to encrypte
def encrypt(w:str):
    global k,index,word
    for i in range(0,len(k)):
        if k[i] == w :
            d=i-index
            print(k[d],end="")

    #a function to run through all the words this could be done in the encrypte function but for a more understandeble way i choose to do this
def stt(w:str):
    s =[]
    for i in w:
        s.append(i)
    d = []     
    for i in s:
        l = encrypt(i)
        d.append(l)
        #user input
word =  input("WORDS: ")
#change the letters to uppercase this part could be done better but am tired to do it
p = word.upper()
#finally calling the function
stt(p)

#if one day someones sees this thank you for looking at my useless coding skils
