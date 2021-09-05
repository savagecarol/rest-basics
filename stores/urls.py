from django.urls import path
from .views import *

urlpatterns = [
    path('', FoodStoreView.as_view()),
    path('<int:pk>', FoodStoreEditView.as_view()),

    path('item', ItemView.as_view()),
    path('item/<int:pk>', ItemEditView.as_view()),
]
