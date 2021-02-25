from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(req):
    return render(req, 'index.html')


def about(req):
    return render(req, 'about.html')


def count(req):
    text = req.GET['text']

    word_list = text.split()
    word_count = len(word_list)

    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    


    return render(req, 'count.html', {'text': text, 'count': word_count, 'worddict': sorted_words})
