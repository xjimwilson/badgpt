from inspect import getfile
import numpy as np
import sys
import saveloadfiles, train, shared, generate

text, choice, loaded = None, None, None

while choice != 't' and choice != 'g':
    choice = input("Enter T to train, or G to generate:\n").lower()

def calcsize(bytesize):
    convsize = bytesize, "bytes"
    if bytesize >= 1000: #1kb:
        convsize = f"{int(bytesize / 1000)} KB"
    if bytesize >= 1000000: #1mb:
        convsize = f"{int(bytesize / 1000000)} MB"
    if bytesize >= 1000000000: #1gb:
        convsize = f"{int(bytesize / 1000000000)} GB"

    return convsize
        

    
if choice == 't':

    while text == None:
        fileinput = str(input("Enter file name:\n"))
        text = saveloadfiles.readfile(fileinput)
      
    print("Training on", calcsize(sys.getsizeof(text)), "of data...")
    train.findngrams(text)
    
    saveloadfiles.savefile(fileinput)

    if fileinput == "":
        fileinput = "fulltrained"
    fileinput.replace("/","")

    print(f"Successfully trained! saved knowledge in memory/{fileinput}.npz, with size of {calcsize(saveloadfiles.getfilesize())}")

elif choice == 'g':
    while loaded == None:
        file = str(input("Enter the file to load:\n"))
        loaded = saveloadfiles.loadfile(file)

    print("File successfully loaded!")

    while True:
        input("\nEnter to generate sentence:\n")


        generate.choosefirstword() #starts generation

        print("\n\n\nWords:", str(shared.wordcounter).replace("\\n","\n"))