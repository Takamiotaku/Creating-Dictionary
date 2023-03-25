import sys
import itertools

Aarguments = ["-v","-h","-p","-d"]
ListofChars = []
Commands = []
Keywords = []
Arg = sys.argv[:]
Arg = Arg[1:]
for i in Arg:
    if i in Aarguments:
        Commands.append(i)
for i in Arg:
    if i not in Aarguments:
        Keywords.append(i)
Name = Keywords[0]
Keywords = Keywords[1:]

#print(Keywords)
#print(Commands)
if Arg[0] not in Aarguments:
    print("Starting Producing a dictionary of words", Keywords , "and saving them in file",Name)
    for string in Keywords:
        ListofChars.extend(list(string))
    combos = itertools.product(ListofChars, repeat=len(ListofChars))
    with open(Name+".txt", 'w') as f:
        for combo in combos:
            f.write(''.join(combo) + '\n')
print("finished")


