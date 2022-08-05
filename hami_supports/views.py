from hami_projects.models import Project
from django.contrib import messages
from .models import Support
from .forms import SupportForm
from datetime import datetime
from django.shortcuts import render, redirect


def support(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    if request.method == 'POST':
        # get project id from project detail page with GET method
        project_id = request.GET.get('project_id')
        selected_project = Project.objects.filter(id=project_id).first()

        support_form = SupportForm(request.POST or None)
        if support_form.is_valid():
            amount = support_form.cleaned_data.get('amount')
            dateN = datetime.now()

            Support.objects.create(amount=amount, project=selected_project, supporter=user, date=dateN)
            total = amount + selected_project.current_budget
            selected_project.current_budget = total
            selected_project.save()
            if selected_project.current_budget > selected_project.budget:
                selected_project.status = 'disable'
                selected_project.save()
            data = {'status': 'ok'}
            request.session['support'] = data
            return redirect(f'/projects/{project_id}')
    else:
        support_form = SupportForm()

    context = {
        'support_form': support_form
    }
    return render(request, 'support.html', context)


def general_support(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    if request.method == 'POST':
        support_form = SupportForm(request.POST or None)
        if support_form.is_valid():
            amount = support_form.cleaned_data.get('amount')
            dateN = datetime.now()
            project_id = request.POST['Radio']
            selected_project = Project.objects.filter(id=project_id).first()
            total = amount + selected_project.current_budget
            selected_project.current_budget = total
            selected_project.save()
            if selected_project.current_budget > selected_project.budget:
                selected_project.status = 'disable'
                selected_project.save()
            Support.objects.create(amount=amount, project=selected_project, supporter=user, date=dateN)
            data = {'status': 'ok'}
            request.session['general_support'] = data
            return redirect('/')
    else:
        support_form = SupportForm()

    projects = Project.objects.filter(status='enable')
    context = {
        'support_form': support_form,
        'projects': projects
    }

    return render(request, 'general_support.html', context)


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