k = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
index = 3
def encrypt(w:str):
    global k,index,word
    for i in range(0,len(k)):
        if k[i] == w :
            d=i-index
            print(k[d],end="")
def stt(w:str):
    s =[]
    for i in w:
        s.append(i)
    d = []     
    for i in s:
        l = encrypt(i)
        d.append(l)
word =  input("WORDS: ")
p = word.upper()
stt(p)
