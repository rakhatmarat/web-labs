from django.urls import path
from api import views
from api.views import VacancyList, VacancyDetail

urlpatterns = [
    path('companies/', views.get_companies),
    path('companies/<int:company_id>', views.get_company),
    path('companies/<int:company_id>/vacancies', views.vacancies_by_company),
    path('vacancies/', VacancyList.as_view()),
    path('vacancies/<int:pk>', VacancyDetail.as_view()),
    path('vacancies/top_ten/', views.top_ten)
]
