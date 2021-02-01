from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import RepoForm, EditForm
from django.views.generic import CreateView

from .models import User, Repo, Tag

def index(request):
    
    if "repos" not in request.session:
        request.session["repos"] = []
    
    return render(request, "network/index.html", {
        "repos": Repo.objects.all(),
        "tags": Tag.objects.all()
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def repo(request, repo_id):
        repo = request.user.repos.get(id=repo_id)
        error = ""
        form_name = RepoForm(request.POST)
        form_del = RepoForm(request.POST)
        form_edit = RepoForm(request.POST)
        form_new = EditForm(request.POST)

        if request.method == "POST":

            if 'Add' in request.POST:
                
                if form_name.is_valid():
                    
                    name = form_name.cleaned_data["name"]
                    tag = Tag(name=name.lower())
                    allTags = repo.tags.all()
                    
                    for old in allTags:

                        if tag.name == old.name:
                            error = "Tag already used"
                            return render(request, "network/repo.html", {
                                "repo" : repo,
                                "form_name" : form_name,    
                                "error" : error,
                                "form_del" : form_del,
                                "form_edit" : form_edit,
                                "form_new" : form_new,
                            })
                    
                    tag.save()
                    tag.repo.add(repo_id)
                                    
                    return render(request, "network/repo.html",{
                        "repo" : repo,
                        "form_name": form_name,
                        "error" : error,
                        "form_del" : form_del,
                        "form_edit" : form_edit,
                        "form_new" : form_new,
                    })
                else:
                    return render(request, "network/repo.html",{
                        "repo" : repo,
                        "form_name": form_name,
                        "error" : error,
                        "form_del" : form_del,
                        "form_edit" : form_edit,
                        "form_new" : form_new,
                    }) 
            elif 'delete' in request.POST:              

                if form_del.is_valid():               
                    
                    name = form_del.cleaned_data["name"]
                    
                    try:
                        tag = Tag.objects.get(name = name.lower())
                        tag.delete()

                        return render(request, "network/repo.html",{
                            "repo" : repo,
                            "form_name": form_name,
                            "error" : error,
                            "form_del" : form_del,
                            "form_edit" : form_edit,
                            "form_new" : form_new,
                        }) 
                    except: 
                        error = "Can't find this tag to be deleted."

                        return render(request, "network/repo.html",{
                            "repo" : repo,
                            "form_name": form_name,
                            "error" : error,
                            "form_del" : form_del,
                            "form_edit" : form_edit,
                            "form_new" : form_new,
                        }) 
                else:  
                    return render(request, "network/repo.html",{
                        "repo" : repo,
                        "form_name": form_name,
                        "error" : error,
                        "form_del" : form_del,
                        "form_edit" : form_edit,
                        "form_new" : form_new,
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
                                "form_name": form_name,
                                "error" : error,
                                "form_del" : form_del,
                                "form_edit" : form_edit,
                                "form_new" : form_new,
                            }) 
                        else: 
                            error = "new name is invalid"
                            return render(request, "network/repo.html",{
                                "repo" : repo,
                                "form_name": form_name,
                                "error" : error,
                                "form_del" : form_del,
                                "form_edit" : form_edit,
                                "form_new" : form_new,
                    }) 
                    except: 
                        error = "No tag with this name to be changed"

                        return render(request, "network/repo.html",{
                            "repo" : repo,
                            "form_name": form_name,
                            "error" : error,
                            "form_del" : form_del,
                            "form_edit" : form_edit,
                            "form_new" : form_new,
                        }) 
                else: 
                    return render(request, "network/repo.html",{
                        "repo" : repo,
                        "form_name": form_name,
                        "error" : error,
                        "form_del" : form_del,
                        "form_edit" : form_edit,
                        "form_new" : form_new,
                    }) 
        return render(request, "network/repo.html",{
           "repo" : repo,
           "form_name": RepoForm(),
           "error" : error,
           "form_del" : RepoForm(),
           "form_edit" : RepoForm(),
           "form_new" : EditForm(),
        })


