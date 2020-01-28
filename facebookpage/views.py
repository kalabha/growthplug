import facebook
import requests

from allauth.socialaccount.models import SocialToken
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, response, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from facebookpage.forms import FbForm


@login_required
def get_access_token(request, user):
    try:
        token = SocialToken.objects.get(
            account__user=user, account__provider="facebook"
        ).token
        return token
    except SocialToken.DoesNotExist:
        logout(request.user)
        messages.add_message(request, messages.ERROR, 'Session Expired. Please login to continue.')
        return HttpResponseRedirect('accounts/login/')


@login_required
def index(request):
    token = get_access_token(request, request.user)

    graph = facebook.GraphAPI(
        access_token=token,
        version="3.1",
    )
    account = graph.get_object(
        "/me/accounts", fields="name,about,description"
    )
    form = FbForm()
    return render(
        request, "index.html", context={"data": account["data"], "form": form}
    )


@login_required
def get_page(request):
    token = get_access_token(request, request.user)

    graph = facebook.GraphAPI(
        access_token=token,
        version="3.1",
    )
    page_id = request.GET.get("id", False)
    page_url = "/" + page_id
    data = graph.get_object(page_url, fields="access_token,about,description")
    return JsonResponse(data)


@login_required
def update_page(request):
    if request.method == "POST":
        page_id = request.POST.get("id", False)
        r = requests.post(
            url=f"https://graph.facebook.com/v5.0/{page_id}",
            params={
                "access_token": request.POST.get("access_token", ""),
                "about": request.POST.get("about", ""),
                "description": request.POST.get("description", ""),
            },
        )
        if r.status_code == 200:
            messages.add_message(request, messages.SUCCESS, 'updated!!')
        else:
            messages.add_message(request, messages.ERROR, r.json()['error']['message'])

        return HttpResponseRedirect("/")

    return HttpResponse(status=405)
