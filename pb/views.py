from django.shortcuts import render
from django.http import HttpResponse
import hashlib


def home_page(request):
    if request.method == "POST":
        return render(request, "home.html", {"pastebin_url": "http://localhost:8000/" +
                            hashlib.md5(request.POST["pastebin_text"]
                                        .encode("utf-8")).hexdigest()})
    return render(request, "home.html")
