from django.shortcuts import render
from django.http import HttpResponse
import hashlib

from pb.models import Pastebin


def home_page(request):
    if request.method == "POST":
        id = hashlib.md5(request.POST["pastebin_text"]
                         .encode("utf-8")).hexdigest()
        pastebin = Pastebin()
        pastebin.text = request.POST.get("pastebin_text", "")
        pastebin.id = id
        pastebin.save()
        return render(request,
                      "home.html",
                      {"pastebin_url": "http://localhost:8000/" + id})
    return render(request, "home.html")
