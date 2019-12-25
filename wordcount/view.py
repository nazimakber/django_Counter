from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return HttpResponse('Hello')

def nazim(request):
	return HttpResponse('<h1>Welcome to the home page of Nazim</h1>')

def asif(request):
	return render(request,'home.html', {'name':'Nazim Akber Ali', 'calc':2+5+9+2545})

def count(request):
	namevalue =	request.GET['fullname']
	words = namevalue.split()
	worddictionary ={}
	for word in words:
		if word in worddictionary:
			worddictionary[word] +=1
		else:
			worddictionary[word] = 1

	sortedWords = sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=True)
	return render(request,'count.html', {'age':'1800 d','hahaha':namevalue,'words':len(words), 'dictionary':worddictionary.items(), 'sorted':sortedWords})

def abouts(request):
	return render(request, 'about.html', {'name':'Nazim'})
	