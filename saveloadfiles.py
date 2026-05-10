import os
import numpy as np
import shared, train
from tkinter import CURRENT

def openfolder(folder):
    readfiles = ""

    for root, dirs, files in os.walk(f"datasets{folder}"):
        for filename in files:
            print(f"Reading {filename}...")
            file_path = os.path.join(root, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                currentfile = f.read().lower()
                readfiles = f"{readfiles}\n{currentfile}" # adds new file to the total read files
    return readfiles

def readfile(file):
    #file = file.strip() #why not

    if file == "":
        return openfolder("")
    elif file[0] == ('/'):
        return openfolder(file)
    
    elif ".txt" not in file:
        file = file + ".txt" # just in case user does not input .txt

    try:
        f = open(f"datasets/{file}", 'r', encoding="utf-8")
        return f.read().lower()
    except:
        print("Could not find file",file)
        return None


def savefile(file):
    if file == "": file = "fulltrained" #defaults to fulltrained.npy when empty
    
    else:
        file = file.replace(".txt",'')

        shared.filepath = f"memory/{file}"

        np.savez_compressed(str(shared.filepath), startersresult = train.startersresult, pairsresult = train.pairsresult, tripletsresult = train.tripletsresult, quadrupletsresult = train.quadrupletsresult, pentupletsresult = train.pentupletsresult)
        #saves as .npz (finding out compression was like discovering fire)

def loadfile(file):
    global result

    if ".npz" not in file:
        file = file + ".npz" # just in case user does not input .npz

    if file == "":
        file = "fulltrained"

    try:
        data = np.load(f"memory/{file}")

        #load into shared variables while converting to lists to avoid numpy type issues

        shared.startersresult = [tuple(row) for row in data["startersresult"]]
        print("Loaded",len(shared.startersresult),"sentence starters")

        shared.pairsresult = [tuple(row) for row in data["pairsresult"]]
        print("Loaded",len(shared.pairsresult),"bigrams")
        shared.tripletsresult = [tuple(row) for row in data["tripletsresult"]]
        print("Loaded",len(shared.tripletsresult),"trigrams")
        shared.quadrupletsresult = [tuple(row) for row in data["quadrupletsresult"]]
        print("Loaded",len(shared.quadrupletsresult),"quadragrams")
        shared.pentupletsresult = [tuple(row) for row in data["pentupletsresult"]]
        print("Loaded",len(shared.pentupletsresult),"pentagrams")

        #load into dicts

        print("loading sentence starters into dictionary form...")
        shared.starters_dict = {}
        for freq, a in shared.startersresult:
            if "starters" not in shared.starters_dict:
                shared.starters_dict["starters"] = []
            shared.starters_dict["starters"].append((a, int(freq)))
            


        print("loading bigrams into dictionary form...")
        shared.pairs_dict = {}
        for freq, a, b in shared.pairsresult:
            if a not in shared.pairs_dict:
                shared.pairs_dict[a] = []
            shared.pairs_dict[a].append((b, int(freq)))

        print("loading trigrams into dictionary form...")
        shared.triplets_dict = {}
        for freq, a, b, c in shared.tripletsresult:
            key = (a,b)
            if key not in shared.triplets_dict:
                shared.triplets_dict[key] = []
            shared.triplets_dict[key].append((c, int(freq)))

        print("loading quadragrams into dictionary form...")
        shared.quadruplets_dict = {}
        for freq, a, b, c, d in shared.quadrupletsresult:
            key = (a, b, c)
            if key not in shared.quadruplets_dict:
                shared.quadruplets_dict[key] = []
            shared.quadruplets_dict[key].append((d, int(freq)))

        print("loading pentagrams into dictionary form...")
        shared.pentuplets_dict = {}
        for freq, a, b, c, d, e in shared.pentupletsresult:
            key = (a, b, c, d)
            if key not in shared.pentuplets_dict:
                shared.pentuplets_dict[key] = []
            shared.pentuplets_dict[key].append((e, int(freq)))

        data.close() #closes afterwards to free up memory

        print("Sucessfully loaded",file)
        return True #signals it went alright

    except:
        print("Could not load",file)
        return #returns nothing so it stays as None


def getfilesize():
    return os.path.getsize(f"{shared.filepath}.npz")