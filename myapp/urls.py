from django.urls import path

from myapp import views

urlpatterns = [
    path('question/', views.question_list, name='question_list'),
    path('question/<int:pk>/', views.choice_list, name='choice_list'),
]