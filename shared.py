import numpy as np

wordcounter = 0

finalsentence = [] #stores generated data

#stores trained data
startersresult = ""

pairsresult = ""
tripletsresult = ""
quadrupletsresult = ""
pentupletsresult = ""

filepath = ""


starters_dict = {}

pairs_dict = {}
triplets_dict = {}
quadruplets_dict = {}
pentuplets_dict = {}

# One day i found out about dictionaries and realised i could use it for data. Switching from searching the database with a for loop
# to a dictionary was probably the biggest scientific revelation since the vaccine. Generation times went from 10 mins to less than 0.1
# of a second. Thank you so much dictionaries.