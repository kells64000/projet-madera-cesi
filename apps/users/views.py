from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render
from django.utils.translation import ugettext_lazy as _

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .forms import ProfileForm, UserForm
from .models import MaderaUser
from .serializers import MaderaUserSerializer


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@csrf_exempt
def user_list(request):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        maderausers = MaderaUser.objects.all()
        serializer = MaderaUserSerializer(maderausers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MaderaUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_detail(request, pk):
    """
    Retrieve, update or delete a user.
    """
    try:
        maderauser = MaderaUser.objects.get(pk=pk)
    except MaderaUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MaderaUserSerializer(maderauser)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MaderaUserSerializer(maderauser, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        maderauser.delete()
        return HttpResponse(status=204)
