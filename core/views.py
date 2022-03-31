from django.shortcuts import render
from core.models import *
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q


def home(request):
    if request.method == 'GET' and request.GET.get('q') is not None:
        q = request.GET.get('q')
        object_list = Publish.objects.filter(
            (
                Q(article__title__icontains = q) |
                Q(author__first_name__icontains = q) |
                Q(author__last_name__icontains = q) |
                Q(category__name__icontains = q)
            )
        ).distinct()
    else:
        q = ''
        object_list = Publish.objects.all()

    page = request.GET.get("page", 1)
    paginator = Paginator(object_list, 10)
    try:
        object_list = paginator.page(page)
    except Exception as error:
        pass

    return render(
        request,
        'home.html',
        {
            'object_list': object_list,
            'paginator': paginator,
            'search': q,
        }
    )

def single(request, slug):
    return render(request, 'generic.html')
