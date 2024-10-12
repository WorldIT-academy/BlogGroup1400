from django.shortcuts import render

# Create your views here.
def render_all_posts(request):
    return render(request, "post_app/all_posts.html")

def render_view_post(request):
    return render(request, "post_app/view_post.html")