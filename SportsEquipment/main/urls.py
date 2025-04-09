from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name ="index"),
      path("user-predata/", views.userpredata, name ="userpredata"),
    path("users-base/", views.user_base, name ="user_base"),
    path("users/borrow/", views.user_borrow, name ="user_borrow"),
    path("users/equipmentDetails/", views.user_equipmentDetails, name ="user_equipmentDetails"),
    path("users/preRequestDetails/", views.user_preRequestDetails, name="user_preRequestDetails"),
       path("users/postRequestDetails/<str:get_request_code>", views.user_postRequestDetails, name="user_postRequestDetails"),
    path("admin-base/", views.admin_base, name ="admin_base"),
    path("admin-login/", views.admin_login, name ="admin_login"),
    #admin-dashboard
    path("admin-dashboard/approve", views.admin_approve_request, name ="admin_approve_request"),
     path("admin-dashboard/denide", views.admin_denied_request, name ="admin_denied_request"),
      path("admin-dashboard/returned", views.admin_returned_request, name ="admin_returned_request"),

     
    path("admin-dashboard/", views.admin_dashboard, name ="admin_dashboard"),
      path("admin-check-request/<str:code>", views.admin_chkdetails, name ="admin_chkdetails"),
        path("admin-check-request-approve/<str:code>", views.admin_chkdetails_app, name ="admin_chkdetails_app"),
         path("admin-equipment-details/", views.admin_equipment_details, name ="admin_equipment_details"),
          path("admin-equipment-details/get/<str:get_equipment_name>", views.admin_equipment_details_invdiv, name ="admin_equipment_details_invdiv"),

            #INITIALIZED
        path('Initialized/cookies/', views.set_csrf_token,  name="set_csrf_token"),
]
