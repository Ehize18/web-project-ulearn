from django.shortcuts import render
from .from_df import sby_dct, cby_dct


def index(request):
    return render(request, "main/index.html")


def relevance(request):
    context = {"salary_table": sby_dct, "count_table": cby_dct}
    return render(request, "main/relevance.html", context=context)