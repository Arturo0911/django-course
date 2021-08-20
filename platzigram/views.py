"""Platzigram views"""

# Django
from django.http import HttpResponse


# Utilities
from datetime import datetime
import json


def helloworld(request):
    """Return a greeting."""
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse("Oh, hi! current server time is {}".format(str(now)))


def sorted_integers(request):
    """HI.
        :url: ?numbers=10,24,50,32
    """
    

    numbers = str(request.GET["numbers"]).split(",")
    numbers = [int(number) for number in numbers]
    numbers.sort()
    data_to_respponse = {
        "status": "ok",
        "numbers_sorted":numbers,
        "message": "Integers sorted successfully"

    }
    return HttpResponse(
        json.dumps(data_to_respponse), 
        content_type="application/json"
    )

def say_hi(request, name, age):
    
    if age < 12:
       message = "sorry {} you aren't allowes here".format(name)
    else:
        message = "Hello, {} Welcome to PlatziGram".format(name)

    return HttpResponse(json.dumps(message))
