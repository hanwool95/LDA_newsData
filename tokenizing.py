
import pickle, csv

from soynlp.tokenizer import LTokenizer

print("loading scores_dictionary")
with open('scores_dictionary.pickle', 'rb') as fr:
    scores_dictionary = pickle.load(fr)
    print("load complete")

words_scores = scores_dictionary['words_scores']
noun_scores = scores_dictionary['noun_scores']
text = scores_dictionary['text']

print("making cohesion_scores")
cohesion_scores = {word:score.cohesion_forward for word, score in words_scores.items()}

#%% md

## combined score
# cohesion score substitute

#%%

print("combining scores")
combined_scores = {noun:score + cohesion_scores.get(noun,0)
                  for noun, score in noun_scores.items()}
print("update combining scores")
combined_scores.update({subword:cohesion for subword, cohesion in cohesion_scores.items()
                       if not (subword in combined_scores)})


## tokenizing

#%%
print("making tokenizer object")
ltokenizer = LTokenizer(scores = combined_scores)

#%%
print("making list of words")
words = [ltokenizer.tokenize(sent) for sent in text]
word_list = []

f = open('token_words.csv', 'w', newline="")
wr = csv.writer(f)
for word in words:
    wr.writerow(word)
    word_list.append(word)
f.close()

with open('token_word_list.pickle','wb') as fw:
    pickle.dump(word_list, fw)
    print("dumping complete")


