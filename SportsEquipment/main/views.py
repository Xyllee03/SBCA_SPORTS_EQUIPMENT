from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import ItemRequest, StudentBorrow
# Create your views here.


def index(request):
    context= {}
    return render(request,"main/index.html", context)


def user_base(request):

    context ={}

    return render(request,"main/users/user_base.html", context)

def user_borrow(request):
    if(request.method =="POST"):


        data = json.loads(request.body)
        # ----> FROM HERE GET PASS TO EQUIPMENT DETAILS
        get_data = request.session.get('users_equipment_detail')
        if get_data is None:
            return JsonResponse({"msg": "There is no equipmentrequest"}, status=500)
        else:
            request.session["borrower_profile"] =data
            """
            # HERE PLAN CREATE --> ALGORITHM FOR CODE
            s = StudentBorrow()
            s.student_no = data['student_no']
            s.first_name = data['first_name']
            s.last_name = data['last_name']

            s.save()
            lastobj = StudentBorrow.objects.last()
            #print(get_data)
           
            for data in get_data:
                ir = ItemRequest()
                #get_list = data[0]['Items']  --> this how you get
                #print(data["Items"]["Equipment_name"])
                ir.equipment_name = data["Items"]["Equipment_name"]
                ir.quantity = data["Items"]["Qty"]
                ir.id_student_borrow = lastobj
                ir.save()
            
        # --> UNTIL HERE
            """
            return JsonResponse({"msg": "Request sent!", "redirect_url":"users/preRequestDetails/"}, status=200)
            

    context ={}
    return render(request, "main/users/user_borrow.html", context)


def user_equipmentDetails(request):
    data =""
    try: 
        data = request.session.get('users_equipment_detail')
      
    finally:
        if(request.method =="POST"):
            data = json.loads(request.body)   
           
            request.session['users_equipment_detail'] = data

            return JsonResponse({"msg": "User has been retrieve", "redirect_url":"users/borrow/"}, status=200)
        context ={
            "equipment_details":data
        }
        return render(request, "main/users/user_equipmentDetails.html", context)

def user_preRequestDetails(request):
    context ={}
    return render(request, 'main/users/user_preRequestDetails.html', context)


    
def admin_base(request):

    context ={}

    return render(request,"main/administration_SBCA/admin_base.html", context)

def admin_login(request):
    context ={}

    return render(request,"main/administration_SBCA/admin_login.html", context)



def admin_dashboard(request):
    context ={}

    return render(request,"main/administration_SBCA/admin_dashboard.html", context) 


def admin_chkdetails(request):
    context ={}

    return render(request,"main/administration_SBCA/admin_chk_req.html", context) 


def admin_equipment_details(request):
    context ={}

    return render(request,"main/administration_SBCA/admin_equipment_details.html", context) 
