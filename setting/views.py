from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SiteSettingForm, SiteSliderForm
from .models import SiteSetting, Slider


@login_required()
def site_setting_edit(request):
    if not request.user.is_staff:
        return redirect("/account/login")
    site_settings = SiteSetting.objects.all()
    site_setting_form = SiteSettingForm(initial={
        'title': site_settings.first().title,
        'address': site_settings.first().address,
        'phone': site_settings.first().phone,
        'mobile': site_settings.first().mobile,
        'fax': site_settings.first().fax,
        'email': site_settings.first().email,
        'about_us': site_settings.first().about_us,
        'copy_right': site_settings.first().copy_right,
        'logo_image': site_settings.first().logo_image,
    }) if site_settings.exists() else SiteSettingForm()
    if request.POST:
        if site_settings.exists():
            site_setting = site_settings.first()
            site_setting_form = SiteSettingForm(request.POST, request.FILES)
            if site_setting_form.is_valid():
                site_setting.title = site_setting_form.cleaned_data.get('title')
                site_setting.address = site_setting_form.cleaned_data.get('address')
                site_setting.phone = site_setting_form.cleaned_data.get('phone')
                site_setting.mobile = site_setting_form.cleaned_data.get('mobile')
                site_setting.fax = site_setting_form.cleaned_data.get('fax')
                site_setting.email = site_setting_form.cleaned_data.get('email')
                site_setting.about_us = site_setting_form.cleaned_data.get('about_us')
                site_setting.copy_right = site_setting_form.cleaned_data.get('copy_right')
                site_setting.logo_image = site_setting_form.cleaned_data.get('logo_image')
                site_setting.save()
                return redirect('/account/admin')
        else:
            site_setting_form = SiteSettingForm(request.POST, request.FILES)
            if site_setting_form.is_valid():
                title = site_setting_form.cleaned_data.get('title')
                address = site_setting_form.cleaned_data.get('address')
                phone = site_setting_form.cleaned_data.get('phone')
                mobile = site_setting_form.cleaned_data.get('mobile')
                fax = site_setting_form.cleaned_data.get('fax')
                email = site_setting_form.cleaned_data.get('email')
                about_us = site_setting_form.cleaned_data.get('about_us')
                copy_right = site_setting_form.cleaned_data.get('copy_right')
                logo_image = site_setting_form.cleaned_data.get('logo_image')
                SiteSetting.objects.create(
                    title=title,
                    address=address,
                    phone=phone,
                    mobile=mobile,
                    fax=fax,
                    email=email,
                    about_us=about_us,
                    copy_right=copy_right,
                    logo_image=logo_image,
                )
    context = {
        'site_setting_form': site_setting_form,
        'title': 'ویرایش' if site_settings.exists() else 'ایجاد'
       }
    return render(request, 'site_setting.html', context)


@login_required()
def site_slider(request):
    if not request.user.is_staff:
        return redirect("/account/login")
    else:
        if request.method == "POST":
            site_slider_form = SiteSliderForm(request.POST, request.FILES)
            if site_slider_form.is_valid():
                title = site_slider_form.cleaned_data.get('title')
                image = site_slider_form.cleaned_data.get('image')
                Slider.objects.create(title=title, image=image)
                data = {'status': 'ok'}
                request.session['create_slider'] = data
        else:
            site_slider_form = SiteSliderForm()

        sliders = Slider.objects.all()
        context = {
            'site_slider_form': site_slider_form,
            'sliders': sliders,
        }

        if 'remove_slider' in request.session:
            context['remove_slider'] = request.session['remove_slider']['status']
            del request.session['remove_slider']

    return render(request, 'site_slider.html', context)


@login_required
def remove_slider(request, slider_id):
    if not request.user.is_staff:
        return redirect("/account/login")
    try:
        Slider.objects.get(pk=slider_id).delete()
    except Slider.DoesNotExist:
        return redirect('/site/slider')
    data = {'status': 'true'}
    request.session['remove_slider'] = data
    return redirect('/site/slider')
