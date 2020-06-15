from django.shortcuts import render
#from django.shortcuts import get_object_or_404
#from django.shortcuts import redirect
#from django.urls import reverse 
from .models import Weapon, Ammo
from django.views.generic import View
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDelMixin
from .forms import AmmoForm, WeaponForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q



def main_page(request):
    return render(request, 'inf/Главная.html')

def weapon_list(request):
    weapons = Weapon.objects.all()
    search_name = request.GET.get('search_name')
    search_caliber = request.GET.get('search_caliber')
    search_description = request.GET.get('search_description')

    if search_name != '' and search_name is not None:
        weapons = weapons.filter(name__icontains=search_name)
    elif search_caliber != '' and search_caliber is not None:
        weapons = weapons.filter(caliber__icontains=search_caliber)
    elif search_description != '' and search_description is not None:
        weapons = weapons.filter(description__icontains=search_description)
#    search_query = request.GET.get('search_name', '')

#    if search_query:
#        weapons = Weapon.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query) | Q(caliber__icontains=search_query))
#    else:
#        weapons = Weapon.objects.all()

    paginator = Paginator(weapons, 5)#обратная замена qs на weapons

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context  ={
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'queryset': weapons
    }
    return render(request, 'inf/weaponls.html', context=context)

class WeaponDetail(ObjectDetailMixin, View):
    model = Weapon
    template = 'inf/weapondl.html'

class WeaponCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = WeaponForm
    template = 'inf/weaponcrt.html'
    raise_exception = True

class WeaponUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Weapon
    model_form = WeaponForm
    template = 'inf/weapon_update_form.html'
    raise_exception = True


class WeaponDel(LoginRequiredMixin, ObjectDelMixin, View):
    model = Weapon
    template = 'inf/weapondel.html'
    redirect_url = 'weapon_list_url'
    raise_exception = True

def ammo_list(request):
    ammos = Ammo.objects.all()
    return render(request, 'inf/ammols.html', context={'ammos': ammos})

class AmmoDetail(ObjectDetailMixin, View):
    model = Ammo
    template = 'inf/ammodl.html'

class AmmoCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = AmmoForm
    template = 'inf/ammocrt.html'
    raise_exception = True

class AmmoUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Ammo
    model_form = AmmoForm
    template = 'inf/ammo_update_form.html'
    raise_exception = True

class AmmoDel(LoginRequiredMixin, ObjectDelMixin, View):
    model = Ammo
    template = 'inf/ammodel.html'
    redirect_url = 'ammo_list_url'
    raise_exception = True