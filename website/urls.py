from django.urls import path, include
from .views import *

app_name = "website"
urlpatterns = [
    path('', index, name='homePage',),
    # path('create/', recordCreatView.as_view(), name='record_create'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]