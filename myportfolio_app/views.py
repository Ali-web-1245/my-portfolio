from email import message
from .forms import ContactForm

from django.shortcuts import render,redirect
from .models import Skill, Project ,Contact


def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()

    return render(request, "myportfolio_app/home.html", {
        "skills": skills,
        "projects": projects,
    })

def about(request):
    return render(request, "myportfolio_app/about.html")

def projects(request):
    projects = Project.objects.all()

    for project in projects:
        project.tech_list = [tech.strip() for tech in project.technologies.split(",")]

    return render(request, "myportfolio_app/projects.html", {
        "projects": projects
    })


# def contact(request):
    # if request.method == "POST":
    #     Contact.objects.create(
    #         name=request.POST.get("name"),
    #         email=request.POST.get("email"),
    #         subject=request.POST.get("subject"),
    #         message=request.POST.get("message"),
    #     )
    #     return redirect("portfolio:success")
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("portfolio:success")
    else:
        form = ContactForm()

    return render(request, "myportfolio_app/contact.html", {
        "form": form,
    })
def success(request):
    return render(request, "myportfolio_app/success.html")