from django.shortcuts import redirect

def redirect_infsys(request):
    return redirect('weapon_list_url', permanent=True)