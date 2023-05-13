from django.urls import path

from .views import *
urlpatterns = [
    path('categories/', view=CategoriesView.as_view()),
    path('category/<str:pk>/', view=CategoryView.as_view()),
    path('incomes/', view=InComesView.as_view()),
    path('income/<str:pk>/', view=InComeView.as_view()),
    path('outcomes/', view=OutComesView.as_view()),
    path('outcome/<str:pk>/', view=OutComeView.as_view())
]
