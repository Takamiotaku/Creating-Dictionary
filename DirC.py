import time 
import sys

Flag = False
Arguments = ["-h","-v","word1"]
Keywords = []

def __main__(*argv):
    print("Place Holder") #######################################################################
    
   

def __counting__(Arguments):
    global Keywords
    num = len(Arguments)
    print("Place Holder") #######################################################################
    for i in range (num):
        Keywords[i] =  __detect__(Arguments[i])
        


#Function dectecs if 
def __detect__(Temp):
    global Flag
    for i in range(len(Arguments)):
        if Temp == Arguments[i]:
            print("Flag is true")
            Flag = True
            return Arguments[i]
        
    if Flag == False:
        print("Flag is false")
        return Temp
    

def __create__ (*arg):
    print(arg)
    
def __commands__ (com):
    #print("comands" + com )
    match com:
        case "-v":
            __version__()
        case "-h":
            __help__()
        case "-b":
            __block__()

def __version__ ():
    print("version")    

def __help__():
    print("help page")

def __block__():
    print("block")


def __Temp__():
    print("x")
 #print ("Number of arguments: ", len(sys.argv))
    if len(sys.argv) == 1:
        print("Invalid amout of arguments: try -h")
    if len(sys.argv) == 2:
        print(sys.argv[1])
        choice = __detect__(sys.argv[1])
        #print("2") 1 is script 2 is arg
        if Flag == True: #commamd
            __commands__(__detect__(choice))
        if Flag == False: #keyword
             __create__(__detect__(choice))
    if len(sys.argv) ==3:
        choice = __detect__(sys.argv[2])
        if Flag == True: #command
            print("command")
        if Flag == False: # keyword
            print("keyword")
    else:
        print("more then 2")

def newfunction()
__main__()

#test for git

