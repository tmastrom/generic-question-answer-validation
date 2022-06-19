from collections import defaultdict
from gensim import corpora, models, similarities

def semantic_transform(text_corpus):
  # Create a set of frequent words 
  stoplist = set('for a of the and to in used has it that can is with like or'.split(' '))
  # lowercase each document, split it by whitespace and filter out stopwords
  texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in text_corpus]

  # count word frequencies
  frequency = defaultdict(int)
  for text in texts:
    for token in text:
      frequency[token] += 1

  texts = [
          [token for token in text if frequency[token] >1]
          for text in texts
  ]

  dictionary = corpora.Dictionary(texts)
  corpus = [dictionary.doc2bow(text) for text in texts]
  lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

  index = similarities.MatrixSimilarity(lsi[corpus]) # transform corpus to LSI space and index it
  return dictionary, lsi, index


def checkAnswer(dictionary, lsi, index, answer):
  vec_bow = dictionary.doc2bow(answer.lower().split())
  vec_lsi = lsi[vec_bow]

  sims = index[vec_lsi]  # perform a similarity query against the corpus
  sims = sorted(enumerate(sims), key=lambda item: -item[1])
  print("Your answer is {} % correct".format(round(sims[0][1]*100, 1)))
  return round(sims[0][1]*100, 1)
