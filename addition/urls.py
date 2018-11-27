from django.urls import path
from .views import AdditionView

urlpatterns = [
	path('',AdditionView.as_view())
]

