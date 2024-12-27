from django.shortcuts import redirect, render
from django.http import HttpResponse
import hashlib

from pb.models import Pastebin

BASE_URL = "/"


def home_page(request):
    if request.method == "POST":
        id = hashlib.md5(request.POST["pastebin_text"]
                         .encode("utf-8")).hexdigest()
        pastebin = Pastebin()
        pastebin.text = request.POST.get("pastebin_text", "")
        pastebin.id = id
        pastebin.save()
        return redirect(BASE_URL + id)
    return render(request, "home.html")


def pastebin_page(request, id):
    return render(request, "pastebin.html", {"id": id})
