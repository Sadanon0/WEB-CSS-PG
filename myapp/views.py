from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def f1(request):
	return render(request, 'padthai.html')

def f2(request):
	return render(request, 'mee.html')

def f3(request):
	return render(request, 'fish.html')

def manager(request):
	return render(request, 'manager.html')