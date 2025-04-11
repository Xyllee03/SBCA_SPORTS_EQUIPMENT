from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import ItemRequest, StudentBorrow, UserSites, REQUESTAPPROVE 
import random
import string
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
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
   
    get_profile = StudentBorrow.objects.filter(code_request =get_request_code).first()
    if get_profile:
        equipments_obj = ItemRequest.objects.filter(id_student_borrow = get_profile)
    try:
      
        del request.session['request_code']
        del request.session['borrower_profile']
        del request.session['users_equipment_detail']
       
    finally:
        
       
  

        context ={
        "Equipments": equipments_obj,
        "Profile":get_profile,
    }
        return render(request, 'main/users/user_postRequestDetails.html', context)

def admin_base(request):

    context ={}

    return render(request,"main/administration_SBCA/admin_base.html", context)



def admin_login(request): 
    if(request.method =="POST"):
        data = json.loads(request.body) 
        print(data) 
        try:
            u_check =  User.objects.get(username =data['username'])
            #print(check_password(data['password'], u_check.password))
            if(check_password(data['password'], u_check.password)):
                user = authenticate(request, username = data['username'], password = data['password'])
                #print("not been authenticate")
                login(request, user)
                print("been authenticate")
                return JsonResponse({"msg": "User has been retrieve", "redirect_url":"/admin-dashboard/"}, status=200)
            
            
            else:
                return JsonResponse({'err':"Wrong username and password"}, status =500)
                
        except:
            return JsonResponse({'err':"Wrong username and password"}, status =500)
       
    context ={}

    return render(request,"main/administration_SBCA/admin_login.html", context)


@login_required
def admin_dashboard(request):

    
    get_user_request = StudentBorrow.objects.filter(request_status = REQUESTAPPROVE.PENDING).order_by("id")
    get_user_approve_request = StudentBorrow.objects.filter(request_status = REQUESTAPPROVE.APPROVE).order_by("id")
    #print(get_user_request)    
    context ={
        "user_request":get_user_request,
        "user_approve": get_user_approve_request
    }

    return render(request,"main/administration_SBCA/admin_dashboard.html", context) 

@login_required
def admin_approve_request(request):
    
    if request.method =="POST":
       
        data = json.loads(request.body)
        #print(data)
        #print("this is for request")
        get_data = StudentBorrow.objects.filter(code_request= data['code']).first()
        
        get_data.request_status = REQUESTAPPROVE.APPROVE
        get_data.save()
     

        return JsonResponse({"msg": "User has been retrieve"}, status=200)

@login_required
def admin_denied_request(request):
    
    if request.method =="POST":
       
        data = json.loads(request.body)
        #print(data)
        #print("this is for request")
        get_data = StudentBorrow.objects.filter(code_request= data['code']).first()
        
        get_data.request_status = REQUESTAPPROVE.DENIED
        get_data.delete()
     

        return JsonResponse({"msg": "User has been retrieve"}, status=200)
@login_required
def admin_returned_request(request):
    if(request.method =="POST"):
  
        data = json.loads(request.body)

        get_user = StudentBorrow.objects.get(code_request =data['code'])
        get_user.delete()

        
        #print(data)
        return JsonResponse({"msg": "User has been retrieve","redirect_url":'/admin-dashboard/'}, status=200)


@login_required
def admin_chkdetails(request, code):
    get_user = StudentBorrow.objects.get(code_request = code)
    get_items = ItemRequest.objects.filter(id_student_borrow = get_user)
    context ={

        "get_user": get_user,
        'get_item': get_items
    }

    return render(request,"main/administration_SBCA/admin_chk_req.html", context) 

@login_required
def admin_chkdetails_app(request, code):
   
    #For input
    if(request.method =="POST"):
        try:
            get_user = StudentBorrow.objects.get(code_request = code)
            return JsonResponse({"msg": "User has been retrieve","redirect_url":f'/admin-check-request-approve/{code}'}, status=200)
        except:
            return JsonResponse({"msg": "Code doesnt exist"}, status=500)

    get_user = StudentBorrow.objects.get(code_request = code)
    get_items = ItemRequest.objects.filter(id_student_borrow = get_user)
    context ={
        
        "get_user": get_user,
        'get_item': get_items
    }
    return render(request,"main/administration_SBCA/admin_chk_req_app.html", context) 
    

@login_required
def admin_equipment_details(request):
    items=['Basketball','Volleyball','Chessboard','Table Tennis Racket','Arnis','Baseball Bat']
    context_arr =[]
    total_items =0
    for item in items:
        get_objs = ItemRequest.objects.filter(equipment_name = item,id_student_borrow__request_status = REQUESTAPPROVE.APPROVE)
        for obj in get_objs:
            total_items += obj.quantity
        context_arr.append({"Equipment_name":item, "total_qty":total_items})
        total_items=0
        #print(context_arr)
    #print(context_arr)   
    #print(context)
    context ={
        "get_data": context_arr
    }
    return render(request,"main/administration_SBCA/admin_equipment_details.html", context)


@login_required
def admin_equipment_details_invdiv(request,get_equipment_name):
    get_specific_items = ItemRequest.objects.filter(equipment_name= get_equipment_name,id_student_borrow__request_status = REQUESTAPPROVE.APPROVE)
    context ={
        "items":get_specific_items,
        "equipment_name": get_equipment_name
    } 
    return render(request,"main/administration_SBCA/admin_equipment_details_indiv.html", context)


@ensure_csrf_cookie
def set_csrf_token(request):
    return JsonResponse({"message": "CSRF token set"})


def custom_404_view(request, exception):
    return render(request, 'main/users/404.html', status=404)