from django.shortcuts import get_object_or_404, render, HttpResponseRedirect)
from .models import Post, Comments
from .forms import PostForm


# Create your views here.
def create_post_view(request):
    context = {}

    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['form'] = form
        return render(request, "create_post.html", context)
    

def post_list_view(request):
    context = {}
    context["dataset"] = Post.objects.all()
    return render(request, "post_list.html", context)


def post_detail_view(request, id):
    context = {}
    context["data"] = Post.objects.get(id = id)
    return render(request, "post_detail.html", context)

def post_update_view(request, id):
    context = {}
    obj = get_object_or_404(Post, id = id)
    form = Post(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    
    context["form"] = form
    return render(request, "post_update.html", context)

def post_delete_view(request, id)
    context = {}
    obj = get_object_or_404(Post, id = id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "post_delete.html", context)