from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import ItemRequest, StudentBorrow
import random
import string
# Create your views here.


def index(request):
    context= {}
    return render(request,"main/index.html", context)


def user_base(request):

    context ={}

    return render(request,"main/users/user_base.html", context)

def userpredata(request):
    if(request.method=="POST"):
        data = json.loads(request.body)
        request.session["borrower_profile"] =data
        return JsonResponse({"msg": "Request sent!", "redirect_url":"users/equipmentDetails/"}, status=200)

def user_borrow(request):
    if(request.method =="POST"):


        data = json.loads(request.body)
        # ----> FROM HERE GET PASS TO EQUIPMENT DETAILS
        get_data = request.session.get('users_equipment_detail')
        if get_data is None:
            return JsonResponse({"msg": "There is no equipment request"}, status=500)
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
    try:
        get_data = request.session.get('borrower_profile')
        context ={
            'Profile':get_data
        }
        print(context)
    finally:
    
 
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

def generate_unique_code():
    characters = string.ascii_uppercase + string.digits  
    while True:
        create_code = ''.join(random.choices(characters, k=12))
        if not StudentBorrow.objects.filter(code_request=create_code).exists():
            return create_code  

def user_preRequestDetails(request):
    profile = request.session.get("borrower_profile")
    equipment_details = request.session.get("users_equipment_detail")
    #Code Generator
   
    print(profile)
    print(equipment_details)
   
    if(request.method =="POST"):
        
        create_code = generate_unique_code()
        request.session['request_code'] = create_code
        s = StudentBorrow()
        s.student_no = profile['student_no']
        s.first_name = profile['first_name']
        s.last_name = profile['last_name']
        s.code_request = create_code
        s.save()
        lastobj = StudentBorrow.objects.last()
        for data in equipment_details:
                ir = ItemRequest()
                #get_list = data[0]['Items']  --> this how you get
                #print(data["Items"]["Equipment_name"])
                ir.equipment_name = data["Items"]["Equipment_name"]
                ir.quantity = data["Items"]["Qty"]
                ir.id_student_borrow = lastobj
                ir.save()



        #print(create_code)
        return JsonResponse({"msg": "User has been retrieve", "redirect_url":f"users/postRequestDetails/{create_code}"}, status=200)
    context ={
        "Profile":profile,
        "Equipment_Details":equipment_details,
        
    }
    #print(context)
    return render(request, 'main/users/user_preRequestDetails.html', context)


def user_postRequestDetails(request, get_request_code):
    #print("This is for request")
    #print(request_code)
    try:
        del request.session['request_code']
        del request.session['borrower_profile']
        del request.session['users_equipment_detail']
    finally:
   
        get_profile = StudentBorrow.objects.get(code_request =get_request_code)
        equipments_obj = ItemRequest.objects.filter(id_student_borrow = get_profile)
  

        context ={
        "Equipments": equipments_obj,
        "Profile":get_profile,
    }
        return render(request, 'main/users/user_postRequestDetails.html', context)

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
