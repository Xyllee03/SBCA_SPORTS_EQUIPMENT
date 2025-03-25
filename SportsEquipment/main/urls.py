from django.urls import path
from . import views

main_app = "main"
urlpatterns = [
    path("", views.index, name ="index"),
    path("users-base/", views.user_base, name ="user_base"),
    path("users/borrow", views.user_borrow, name ="user_borrow"),
    path("users/equipmentDetails", views.user_equipmentDetails, name ="user_equipmentDetails"),
    path("users/preRequestDetails", views.user_preRequestDetails, name="user_preRequestDetails"),
]
