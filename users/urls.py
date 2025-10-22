from django.urls import path
from users.views import Signup

urlpatterns = [
    path('signup', Signup.as_view()),

]