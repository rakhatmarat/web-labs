import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from api.models import Company, Vacancy, companies, vacancies
# Create your views here.


@csrf_exempt
def get_company(request, company_id):
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    if request.method == "GET":
        return JsonResponse(company.to_json(), status=200)
    elif request.method == "PUT":
        data = json.load(request.body)
        new_name = data.get('name', company.name)
        new_city = data.get('city', company.city)
        new_address = data.get('address', company.address)
        new_description = data.get('description', company.description)
        company.name = new_name
        company.city = new_city
        company.address = new_address
        company.description = new_description
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == "DELETE":
        company.delete()
        return JsonResponse({"deleted": True})


@csrf_exempt
def get_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(pk=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == "GET":
        return JsonResponse(vacancy.to_json(), status=200)
    elif request.method == "PUT":
        data = json.loads(request.body)
        new_name = data.get('name', vacancy.name)
        new_salary = data.get('salary', vacancy.salary)
        new_company = data.get('company', vacancy.company.name)
        new_description = data.get('description', vacancy.description)
        vacancy.name = new_name
        vacancy.salary = new_salary
        vacancy.company = Company.objects.filter(name=new_company).get()
        vacancy.description = new_description
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    elif request.method == "DELETE":
        vacancy.delete()
        return JsonResponse({"deleted": True})


@csrf_exempt
def get_companies(request):
    if request.method == "GET":
        companies_json = [c.to_json() for c in companies()]
        return JsonResponse(companies_json, safe=False)
    if request.method == "POST":
        data = json.loads(request.body)
        comp_name = data.get('name', '')
        comp_city = data.get('city','')
        comp_description = data.get('description', '')
        comp_address = data.get('address', '')
        company = Company.objects.create(name=comp_name, city=comp_city, description=comp_description, address=comp_address)
        return JsonResponse(company.to_json, safe=False)


@csrf_exempt
def get_vacancies(request):
    if request.method == "GET":
        vacancies_json = [v.to_json() for v in vacancies()]
        return JsonResponse(vacancies_json, safe=False)
    if request.method == "POST":
        data = json.loads(request.body)
        vac_name = data.get('name', '')
        vac_salary = data.get('salary',0)
        vac_description = data.get('description', '')
        vac_company = data.get('company', '')
        company_obj = Company.objects.get(pk=1)
        if vac_company != '':
            company_obj = Company.objects.filter(name=vac_company).get()
        vacancy = Vacancy.objects.create(name=vac_name, salary=vac_salary, description=vac_description, company=company_obj)
        return JsonResponse(vacancy.to_json(), safe=False)


def vacancies_by_company(request, company_id):
    company = Company.objects.get(pk=company_id)
    vacancies_json = [v.to_json() for v in vacancies() if v.company.name == company.name]
    return JsonResponse(vacancies_json, safe=False)
