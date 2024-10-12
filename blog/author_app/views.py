from django.shortcuts import render


def render_all_authors(request):
    return render(request, 'author_app/all_authors.html')

def render_view_author(request):
    return render(request, 'author_app/view_author.html')