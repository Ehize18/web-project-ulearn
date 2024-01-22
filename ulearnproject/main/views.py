from django.shortcuts import render
from .from_df import sby_dct, cby_dct
from .skills import all_skills, fullstack_skills


def index(request):
    return render(request, "main/index.html")


def relevance(request):
    context = {"salary_table": sby_dct, "count_table": cby_dct}
    return render(request, "main/relevance.html", context=context)


def geography(request):
    return render(request, "main/geography.html")


def skills(request):
    context = {"all_skills": all_skills, "fullstack_skills": fullstack_skills}
    return render(request, "main/skills.html", context=context)