from hami_projects.models import Project
from django.contrib import messages
from .models import Support, ExtraSupport
from .forms import SupportForm
from datetime import datetime
from django.db.models import F
from django.shortcuts import redirect, render
from django.http import HttpResponse
from zeep import Client

support_info = None

def support(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    #get project id from project detail page with GET method
    project_id = request.GET.get('project_id')
    selected_project = Project.objects.filter(id=project_id).first()

    support_form = SupportForm(request.POST or None)
    if support_form.is_valid():
        price = support_form.cleaned_data.get('price')
        dateN = datetime.now()

        #the support should create after success payment and the support addes to project ((not HERE)) // send info with support_info func
        Support.objects.create(title="حمایت جدید", price=price, project=selected_project,supporter=user, date=dateN)
        total = price + selected_project.Currentـbudget
        selected_project.Currentـbudget = total
        selected_project.save()
        if selected_project.Currentـbudget > selected_project.budget:
            selected_project.status = 'disable'
            selected_project.save()
        messages.success(request, 'حمایت شما با موفقیت انجام شد. :)')
        # global support_info
        # def support_info():
        #     info = {
        #     'selected_project':selected_project, 
        #     'price':price, 
        #     'dateN':dateN, 
        #     'user':user, 
        #     }
        #     return info 


    context = {
        'support_form':support_form
    }
    return render (request, 'support.html', context)


def general_support(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    bank = ExtraSupport.objects.all().first()
    if bank.price > 0:
        ready_to_support = Project.objects.filter(Currentـbudget__lt=F('budget'), status='enable').order_by(
            '-order').first()
        if ready_to_support:
            needed_price = ready_to_support.budget - ready_to_support.Currentـbudget
            if bank.price >= needed_price:
                ready_to_support.Currentـbudget = ready_to_support.Currentـbudget + needed_price
                ready_to_support.save()
                bank.price = bank.price - needed_price
                bank.save()
                dateN = datetime.now()
                Support.objects.create(title="حمایت جدید", price=ready_to_support.Currentـbudget, project=ready_to_support,
                                       supporter=user, date=dateN)
            else:
                ready_to_support.Currentـbudget = ready_to_support.Currentـbudget + bank.price
                ready_to_support.save()
                bank.price = 0
                bank.save()
                dateN = datetime.now()
                Support.objects.create(title="حمایت جدید", price=ready_to_support.Currentـbudget,
                                       project=ready_to_support, supporter=user, date=dateN)

    support_form = SupportForm(request.POST or None)
    if support_form.is_valid():
        price = support_form.cleaned_data.get('price')
        dateN = datetime.now()

        #the support should create after success payment and the support addes to project ((not HERE)) // send info with support_info func
        ready_to_support = Project.objects.filter(Currentـbudget__lt=F('budget'), status='enable').order_by('-order')
        if not ready_to_support:
            bank = ExtraSupport.objects.all().first()
            total = price + bank.price
            bank.price = total
            bank.save()
            messages.success(request, 'حمایت شما با موفقیت انجام شد. :)')
        else:
            selected_project = ready_to_support.first()
            total = price + selected_project.Currentـbudget
            if total > selected_project.budget:
                resault = total - selected_project.budget
                selected_project.Currentـbudget = selected_project.budget
                selected_project.save()
                bank = ExtraSupport.objects.all().first()
                bank.price = bank.price + resault
                bank.save()
                if selected_project.Currentـbudget >= selected_project.budget:
                    selected_project.status = 'disable'
                    selected_project.save()
                Support.objects.create(title="حمایت جدید", price=price, project=selected_project, supporter=user, date=dateN)
                messages.success(request, 'حمایت شما با موفقیت انجام شد. :)')
            else:
                total = price + selected_project.Currentـbudget
                selected_project.Currentـbudget = total
                selected_project.save()
                if selected_project.Currentـbudget >= selected_project.budget:
                    selected_project.status = 'disable'
                    selected_project.save()
                Support.objects.create(title="حمایت جدید", price=price, project=selected_project, supporter=user, date=dateN)
                messages.success(request, 'حمایت شما با موفقیت انجام شد. :)')


        # global support_info
        # def support_info():
        #     info = {
        #     'selected_project':selected_project,
        #     'price':price,
        #     'dateN':dateN,
        #     'user':user,
        #     }
        #     return info


    context = {
        'support_form':support_form
    }

    return render (request, 'support.html', context)

# MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
#  client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
# amount = 0  # Toman / Required
# description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# email = 'email@example.com'  # Optional
# mobile = '09123456789'  # Optional
# CallbackURL = 'http://localhost:8000/verify' # Important: need to edit for realy server.

# def send_request(request):
#     #get support support from support page from POST request // change action of support form to "/request"

#     # price = float(request.POST.get('price'))
#     # global amount
#     # amount += price
#     # print(amount)

#     result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
#     if result.Status == 100:
#         return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
#     else:
#         return HttpResponse('Error code: ' + str(result.Status))

# def verify(request):
#     #supporter informations to create support in db

#     # support_informations = support_info()
#     # selected_project = support_informations['selected_project']
#     # price = support_informations['price']
#     # dateN = support_informations['dateN']
#     # user = support_informations['user']

#     if request.GET.get('Status') == 'OK':
#         result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
#         if result.Status == 100:
#             return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))

#         elif result.Status == 101:
#             return HttpResponse('Transaction submitted : ' + str(result.Status))
#         else:
#             return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
#     else:
#         return HttpResponse('Transaction failed or canceled by user')