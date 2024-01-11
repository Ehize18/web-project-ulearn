from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def relevance(request):
    return render(request, "main/relevance.html")