import sys
from sklearn.feature_extraction import text
from sklearn import pipeline
from sklearn import linear_model
import numpy

def load_data(filename):
  with open(filename) as f:
      xs = []
      ys = []
      for line in f.readlines()[1:]:
        ys.append(int(line[0]))
        xs.append(line[2:-2])
  return xs, ys

def make_model():
    clf = pipeline.Pipeline([
        #('vec', CountVectorizer()),
        ('tfidf',
         text.TfidfVectorizer(stop_words='english', ngram_range=(1, 1),
                              min_df=4,strip_accents='ascii', lowercase=True)),
        ('clf',
         LinearSVC()
        # linear_model.SGDClassifier(class_weight='balanced')
         )
    ])
    return clf


def run():
    xs, ys = load_data('trainingdataDoc.txt')
    mdl = make_model()
    mdl.fit(xs, ys)

    q = int(input())
    test = [input() for _ in range(q)]
    for y in mdl.predict(test):
      print(y)



corpus = [
    'This is the first document.',
     'This document is the second document.',
     'And this is the third one.',
     'Is this And the first document']
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
pd.DataFrame(X.toarray(),columns=vectorizer.get_feature_names_out())


from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

vocabulary = ['this', 'document', 'first', 'is', 'second', 'the','and', 'one']
pipe = Pipeline([('count', CountVectorizer(vocabulary=vocabulary)), 
                 ('tfid', TfidfTransformer())])
pipe = pipe.fit(corpus)
print(pipe['count'].transform(corpus).toarray())
print(pipe['tfid'].idf_)
print(pipe.transform(corpus).shape)


corpus = ['this is the first document',
          "long day"]
print(pipe['count'].transform(corpus).toarray())
print(pipe['tfid'].idf_)
print(pipe.transform(corpus).shape)