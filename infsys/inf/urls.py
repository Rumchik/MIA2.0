from django.urls import path

from .views import weapon_list, main_page, WeaponDetail, ammo_list, AmmoDetail, AmmoCreate, WeaponCreate, AmmoUpdate, WeaponUpdate, AmmoDel, WeaponDel

urlpatterns = [
    path('', main_page, name='main_url'),
    path('огнестрельное_оружие', weapon_list, name='weapon_list_url'),
    path('огнестрельное_оружие/добавить', WeaponCreate.as_view(), name='weapon_create_url'),
    path('огнестрельное_оружие/<str:slug>', WeaponDetail.as_view(), name='weapon_detail_url'),
    path('огнестрельное_оружие/<str:slug>/редактировать', WeaponUpdate.as_view(), name='weapon_update_url'),
    path('огнестрельное_оружие/<str:slug>/удаление', WeaponDel.as_view(), name='weapon_del_url'),
    path('патроны', ammo_list, name='ammo_list_url'),
    path('патроны/добавить', AmmoCreate.as_view(), name='ammo_create_url'),
    path('патроны/<str:slug>', AmmoDetail.as_view(), name='ammo_detail_url'),
    path('патроны/<str:slug>/редактировать', AmmoUpdate.as_view(), name='ammo_update_url'),
    path('патроны/<str:slug>/удаление', AmmoDel.as_view(), name='ammo_del_url'),
    #path('/газовоое_оружие', gas_weapon_list, name='gas_weapon_list_url'),
    #path('/газовоое_оружие/<str:slug>', GasWeaponDetail.as_view(), name='gas_weapon_detail_url'),
    #path('/газовоое_оружие/добавить', GasWeaponCreate.as_view(), name='gas_weapon_create_url'),
    #path('/пневматическое_оружие', air_weapon_list, name='air_weapon_list_url'),
    #path('/пневматическое_оружие/<str:slug>', AirWeaponDetail.as_view(), name='air_weapon_detail_url'),
    #path('/пневматическое_оружие/добавить', AirWeaponCreate.as_view(), name='air_weapon_create_url'),
    #path('/специальные_средства', sm_list, name='sm_list_url'),
    #path('/специальные_средства/<str:slug>', SMDetail.as_view(), name='sm_detail_url'),
    #path('/специальные_средства/добавить', SMCreate.as_view(), name='sm_create_url'),
    ]

