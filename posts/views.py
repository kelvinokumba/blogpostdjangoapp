from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
posts=[
    {
        "id":1,
        "title":"Learn django",
        "author":"Ssali"
    },
    {  
        "id":2,
        "title":"Learn Flask",
        "author":"Ssali"
    }, 
    
    {
        "id":3,
        "title":"Learn Javascrpit",
        "author":"code mosh"
    }
  
]



def index(request:HttpRequest):
    name= request.GET.get("name") or "world"
    
    context={
        "name": name
    }

    return render(request,'index.html',context)


def greet(request:HttpRequest):
    name= request.GET.get("name") or "world"
    
    return HttpResponse(f"Hello {name}")

def return_all_posts(request:HttpRequest):
    return HttpResponse(str(posts))

def return_one_post(request:HttpRequest, post_id):
    for post in posts:
        if post["id"]==post_id:
        
            return HttpResponse(str(post))
        
    return HttpRequest("Not Found")
