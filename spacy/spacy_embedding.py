#coding=utf-8
__author__ = 'liyang54'
import nlp_tool.spacy
from nlp_tool.spacy import displacy

#embedding
# nlp = nlp_tool.spacy.load('en')
nlp = nlp_tool.spacy.load('en_core_web_lg')
print(nlp.vocab['minister'].vector)
dog = nlp.vocab["dog"]
cat = nlp.vocab["cat"]
apple = nlp.vocab["apple"]
orange = nlp.vocab["orange"]
print(dog.similarity(cat))
print(dog.similarity(orange))