from django.shortcuts import render
from .get_vacancies import vacancies

def last_vacancies(request):
    context = {"vacancies" : vacancies}
    return render(request, "last_vacancies/last_vacancies.html", context=context)
