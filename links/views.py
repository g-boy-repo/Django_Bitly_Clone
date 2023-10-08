from django.shortcuts import get_object_or_404, render, redirect

from .models import Link

# Create your views here.


def index(request):
    links = Link.objects.all()
    context = {
        'links': links
    }
    return render(request, 'links/index.html', context)


def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()  # increment the link's click count

    return redirect(link.url)


def add_link(request):
    return render(request, 'links/create.html', {})
