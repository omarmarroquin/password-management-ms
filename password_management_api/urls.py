from django.urls import path
from password_management_api.views import PasswordCardList, PasswordCardDetail

urlpatterns = [
  path('password-cards/', PasswordCardList.as_view()),
  path('password-cards/<int:id>', PasswordCardDetail.as_view()),
]