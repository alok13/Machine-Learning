#Step 0
import codecs
import glob
import multiprocessing
import os
import pprint
import re
import nltk
import gensim.models.word2vec as w2v
import sklearn.manifold
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


nltk.download('punkt')
nltk.download('stopwords')

book_filenames=sorted(glob.glob("data/*.txt"))
#print(book_filenames)

corpus_raw =u""
for book_filename in book_filenames:
	#print("Reading '{0}'... ".format(book_filename))
	with codecs.open(book_filename,"r","utf-8") as book_file:
		corpus_raw+=book_file.read()
	print("Corpus is now {0} long".format(len(corpus_raw)) )	
