#CragiListClassify
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

def fs(i):
    return " ".join(" ".join((s + "__" + u) for u in re.findall(r"[A-Za-z0-9]{2,}", i[s])) for s in ("city", "section", "heading"))


def features(d):
    return d['heading'] + d['section']

def training_data():
    with open('training (1).json') as f:
      data = [json.loads(line) for line in f.readlines()[1:]]
    words = [features(d) for d in data]
    classification = [d['category'] for d in data]
    return words, classification

def get_model():
    words, classification = training_data()
    pipe = Pipeline([('vect', CountVectorizer()), 
                     ('tfidf', TfidfTransformer()), 
                     ('clf', LinearSVC())])
       # classifier = svm.LinearSVC().fit(training_tfidf, annotation)
    return pipe.fit(words, classification)

def run():
    model = get_model()
    data = [json.loads(input()) for _ in range(int(input()))]
    words = [features(d) for d in data]
    predictions = model.predict(words)
    print(*predictions, sep='\n')