import signup as signup
from django.contrib import admin
from django.urls import path, include

from accounts.views import SignUPView

urlpatterns = [
    path('signup/', SignUPView.as_view(), name='signup'),
]
