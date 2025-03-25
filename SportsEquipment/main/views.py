from django.shortcuts import render

# Create your views here.


def index(request):
    context= {}
    return render(request,"main/index.html", context)


def user_base(request):

    context ={}

    return render(request,"main/users/user_base.html", context)

def user_borrow(request):
    context ={}
    return render(request, "main/users/user_borrow.html", context)


def user_equipmentDetails(request):
    context ={}
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
