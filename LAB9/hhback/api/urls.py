from django.urls import path
from api import views

urlpatterns = [
    path('companies/', views.get_companies),
    path('companies/<int:company_id>', views.get_company),
    path('companies/<int:company_id>/vacancies', views.vacancies_by_company),
    path('vacancies/', views.get_vacancies),
    path('vacancies/<int:vacancy_id>', views.get_vacancy),
]
