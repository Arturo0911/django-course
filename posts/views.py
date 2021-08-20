from django.shortcuts import render


# Django
from django.http import HttpResponse


# Utilities
from datetime import datetime

posts = [
    {
        "name": "Mont Blanc",
        "user": "Artur Negreiros",
        "time": datetime.now().strftime("%b %dth %Y - %H:%M hrs"),
        "picture": "https://picsum.photos/id/1036/200/200"
    },
    {
        "name": "Brandon",
        "user": "Brandon Samanez",
        "time": datetime.now().strftime("%b %dth %Y - %H:%M hrs"),
        "picture": "https://picsum.photos/id/903/200/200"
    },
    {
        "name": "Nuevo auditorio",
        "user": "Lorem Ipsum",
        "time": datetime.now().strftime("%b %dth %Y - %H:%M hrs"),
        "picture": "https://picsum.photos/id/1076200/200"
    },
]

def list_posts(request):

    content = []
    for post in posts:
        content.append("""  
            <p><strong>{name}</strong></p>
            <p><strong>{user}</strong></p>
           <figure><img src = "picture"
        """)
    return HttpResponse(posts)