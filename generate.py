import random
import shared

maxwords = 50
matchesthreshold = 0.5
datasetformat = "rawtext1.0"


def choosefirstword(): #each model should output firstword
    if datasetformat == "rawtext1.0":
        total_freq = sum(freq for _, freq in shared.starters_dict)
        mean_freq = total_freq / len(shared.starters_dict)
        first_words = []
        weights = []
        for word, freq in shared.starters_dict:
            if freq > mean_freq * matchesthreshold:
                first_words.append(word)
                weights.append(freq)
        if first_words:
            firstword = random.choices(first_words, weights=weights)[0]
                    
    else:
        print("<datasetformat> not recognised")
        return
    

    firstword.strip()
    shared.finalsentence.append(firstword)
    generate(firstword)


def generate(firstword):  # Iterative function for faster generation
    shared.finalsentence = [firstword.lower()]
    shared.wordcounter = 1
    
    print(firstword, end=" ")

    next_word = firstword
    
    while shared.wordcounter < maxwords or next_word[-1] not in ['?', '!', '.', '|']:
        current_word = shared.finalsentence[-1]
        
        next_word = None


        # Try pentuplets
        if len(shared.finalsentence) > 3:
            key = (shared.finalsentence[-4], shared.finalsentence[-3], shared.finalsentence[-2], current_word)
            if key in shared.pentuplets_dict:
                matches = shared.pentuplets_dict[key]
                if matches:
                    total_freq = sum(freq for _, freq in matches)
                    mean_freq = total_freq / len(matches)
                    next_words = []
                    weights = []
                    for word, freq in matches:
                        if freq > mean_freq * matchesthreshold:
                            next_words.append(word)
                            weights.append(freq ** 2)
                    if next_words:
                        next_word = random.choices(next_words, weights=weights)[0]
        
        # Try quadruplets
        if len(shared.finalsentence) > 2:
            key = (shared.finalsentence[-3], shared.finalsentence[-2], current_word)
            if key in shared.quadruplets_dict:
                matches = shared.quadruplets_dict[key]
                if matches:
                    total_freq = sum(freq for _, freq in matches)
                    mean_freq = total_freq / len(matches)
                    next_words = []
                    weights = []
                    for word, freq in matches:
                        if freq > mean_freq * matchesthreshold:
                            next_words.append(word)
                            weights.append(freq ** 2)
                    if next_words:
                        next_word = random.choices(next_words, weights=weights)[0]
        
        # Try triplets
        if next_word is None and len(shared.finalsentence) > 1:
            key = (shared.finalsentence[-2], current_word)
            if key in shared.triplets_dict:
                matches = shared.triplets_dict[key]
                if matches:
                    total_freq = sum(freq for _, freq in matches)
                    mean_freq = total_freq / len(matches)
                    next_words = []
                    weights = []
                    for word, freq in matches:
                        if freq > mean_freq * matchesthreshold:
                            next_words.append(word)
                            weights.append(freq ** 2)
                    if next_words:
                        next_word = random.choices(next_words, weights=weights)[0]
        
        # Try pairs
        if next_word is None:
            if current_word in shared.pairs_dict:
                matches = shared.pairs_dict[current_word]
                if matches:
                    total_freq = sum(freq for _, freq in matches)
                    mean_freq = total_freq / len(matches)
                    next_words = []
                    weights = []
                    for word, freq in matches:
                        if freq > mean_freq * matchesthreshold:
                            next_words.append(word)
                            weights.append(freq)
                    if next_words:
                        next_word = random.choices(next_words, weights=weights)[0]
        
        if next_word is None:
            print("\n\nCould not find a match for word. Ending generation.")
            return
        


        if shared.finalsentence[-1][-1] in ['?', '!', '.', '|']:
            print(next_word.capitalize(), end=" ")
        else:
            print(next_word, end=" ")

        shared.finalsentence.append(next_word)      
        shared.wordcounter += 1
        
