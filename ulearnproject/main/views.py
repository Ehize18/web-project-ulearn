from django.shortcuts import render
from .relevance import sby_dct, cby_dct
from .skills import all_skills, fullstack_skills
from .geography import *


def index(request):
    return render(request, "main/index.html")


def relevance(request):
    context = {"salary_table": sby_dct, "count_table": cby_dct}
    return render(request, "main/relevance.html", context=context)


def geography(request):
    context = {"geo_all_count": geo_all_count, "geo_fullstack_count": geo_fullstack_count,
               "geo_all_salary": geo_all_salary, "geo_fullstack_salary": geo_fullstack_salary}
    return render(request, "main/geography.html", context=context)


def skills(request):
    context = {"all_skills": all_skills, "fullstack_skills": fullstack_skills}
    return render(request, "main/skills.html", context=context)