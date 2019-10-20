from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):


    qs = BlogPost.objects.all()[:5]
    context = {"title": "Welcome", 'blog_list':qs}

    return render(request,"home.html",context)

def about_page(request):
    return render(request,"about_page.html",{"title":"About Page"})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact Us",
        "form": form
    }
    return render(request, "form.html", context)

def example_page(request):
    context = {"title":"Example"}
    template_name = "home.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))