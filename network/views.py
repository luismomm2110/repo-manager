from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import RepoForm, EditForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
import requests, json

from .models import User, Repo, Tag

@login_required
def index(request):
    
    name = request.user.username 
    r = requests.get(f"https://api.github.com/users/{name}/starred")
    data = json.loads(r.content)
    listId =[]

    for index in data:
        
        repo = Repo(id = index["id"], name = index["name"], description = index["description"], 
                    link = index["html_url"])
        repo.save()
        request.user.repos.add(repo)
        listId.append(index["id"])


    for x in request.user.repos.all():
            if int(x.id) not in listId:
                x.de
        
    return render(request, "network/index.html", {
        "repos": request.user.repos.all(),
        "tags": Tag.objects.all(),
        "data" : listId,
    })

def login_view(request):
    return render(request, "network/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def repo(request, repo_id):
        repo = request.user.repos.get(id=repo_id)
        error = ""
        form_name = RepoForm(request.POST)
        form_del = RepoForm(request.POST)
        form_edit = RepoForm(request.POST)
        form_new = EditForm(request.POST)

        if request.method == "POST":

            if 'add' in request.POST:
                
                if form_name.is_valid():
                    
                    name = form_name.cleaned_data["name"]
                    tag = Tag(name=name.lower())
                    allTags = repo.tags.all()
                    
                    for old in allTags:

                        if tag.name == old.name:
                            error = "Tag already used"
                            return render(request, "network/repo.html",{
                                    "repo" : repo,
                                    "form_name": RepoForm(),
                                    "error" : error,
                                    "form_del" : RepoForm(),
                                    "form_edit" : RepoForm(),
                                    "form_new" : EditForm(),
                            })
           
                    
                    tag.save()
                    tag.repo.add(repo_id)
                    return render(request, "network/repo.html",{
                                "repo" : repo,
                                "form_name": RepoForm(),
                                "error" : error,
                                "form_del" : RepoForm(),
                                "form_edit" : RepoForm(),
                                "form_new" : EditForm(),
                    })
                                    
                   
            elif 'delete' in request.POST:              

                if form_del.is_valid():               
                    
                    name = form_del.cleaned_data["name"]
                    
                    try:
                        tag = Tag.objects.get(name = name.lower())
                        tag.delete()

                        return render(request, "network/repo.html",{
                            "repo" : repo,
                            "form_name": RepoForm(),
                            "error" : error,
                            "form_del" : RepoForm(),
                            "form_edit" : RepoForm(),
                            "form_new" : EditForm(),
                        })
                    
                    except: 
                        error = "Can't find this tag to be deleted."

                    return render(request, "network/repo.html",{
                            "repo" : repo,
                            "form_name": RepoForm(),
                            "error" : error,
                            "form_del" : RepoForm(),
                            "form_edit" : RepoForm(),
                            "form_new" : EditForm(),
                    })
                
                else:  
                    return render(request, "network/repo.html",{
                        "repo" : repo,
                        "form_name": RepoForm(),
                        "error" : error,
                        "form_del" : RepoForm(),
                        "form_edit" : RepoForm(),
                         "form_new" : EditForm(),
                    })

            elif 'edit' in request.POST:              

                if form_edit.is_valid():               
                    
                    name = form_edit.cleaned_data["name"]

                    try:
                        tag = Tag.objects.get(name = name.lower())
                        
                        if form_new.is_valid():
                            tag.delete()
                            newName = form_new.cleaned_data["newName"]
                            newTag = Tag(name = newName.lower())
                            newTag.save()
                            newTag.repo.add(repo_id)

                            return render(request, "network/repo.html",{
                                "repo" : repo,
                                "form_name": RepoForm(),
                                "error" : error,
                                "form_del" : RepoForm(),
                                "form_edit" : RepoForm(),
                                "form_new" : EditForm(),
                            })
                        
                        else: 
                            error = "new name is invalid"
                            return render(request, "network/repo.html",{
                                    "repo" : repo,
                                    "form_name": RepoForm(),
                                    "error" : error,
                                    "form_del" : RepoForm(),
                                    "form_edit" : RepoForm(),
                                    "form_new" : EditForm(),
                             })
                    
                    except: 
                        error = "No tag with this name to be changed"

                        return render(request, "network/repo.html",{
                                "repo" : repo,
                                "form_name": RepoForm(),
                                "error" : error,
                                "form_del" : RepoForm(),
                                "form_edit" : RepoForm(),
                                "form_new" : EditForm(),
                        })
                       
                else: 
                    return render(request, "network/repo.html",{
                            "repo" : repo,
                            "form_name": RepoForm(),
                            "error" : error,
                            "form_del" : RepoForm(),
                            "form_edit" : RepoForm(),
                            "form_new" : EditForm(),
                    })
        
        return render(request, "network/repo.html",{
           "repo" : repo,
           "form_name": RepoForm(),
           "error" : error,
           "form_del" : RepoForm(),
           "form_edit" : RepoForm(),
           "form_new" : EditForm(),
        })


