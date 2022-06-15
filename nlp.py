from collections import defaultdict
from gensim import corpora, models, similarities

# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

text_corpus = [
               "In software development, Python can aid in tasks like build control, bug tracking, and testing. With Python, software developers can automate testing for new products or features. Some Python tools used for software testing include Green and Requestium.",
               "Python has become a staple in data science, allowing data analysts and other professionals to use the language to conduct complex statistical calculations, create data visualizations, build machine learning algorithms, manipulate and analyze data, and complete other data-related tasks.",
               "Data analysis and machine learning",
               "Python is often used to develop the back end of a website or application—the parts that a user doesn’t see. Python’s role in web development can include sending data to and from servers, processing data and communicating with databases, URL routing, and ensuring security. Python offers several frameworks for web development. Commonly used ones include Django and Flask.",
               "Web development", 
               "Automation or scripting",
               "Software testing and prototyping",
               "Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis"
]

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

def checkAnswer(doc):
  vec_bow = dictionary.doc2bow(doc.lower().split())
  vec_lsi = lsi[vec_bow]

  sims = index[vec_lsi]  # perform a similarity query against the corpus
  sims = sorted(enumerate(sims), key=lambda item: -item[1])
  print("Your answer is {} % correct".format(round(sims[0][1]*100, 1)))
  

print("Question: What is Python?")

doc = input("Your answer: ")
checkAnswer(doc)