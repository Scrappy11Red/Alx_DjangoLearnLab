from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .models import Post, Comment
from .forms import PostForm
from rest_framework import serializers
from .serializers import PostSerealizer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, 


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

def post_delete_view(request, id):
    context = {}
    obj = get_object_or_404(Post, id = id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "post_delete.html", context)



@api_view(['GET'])
def CommentOverview(request):
    comment_urls = {
        'all_comments': '/',
        'Add': '/create', 
        'Update': '/update/pk',
        'Delete': '/comment/pk/delete'
    }

    return Response(comment_urls)


@api_view([['POST']])
def create_comments(request):
    comment = CommentSerializer(data=request.data)

    if comment.is_valid():
        comment.save()
        return Response(comment.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def view_comments(request):
    if request.query_params:
        comments = Comment.objects.filter(**request.query_params.dict())
    else:
        comments = Comment.objects.all()

    if comments:
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def update_comments(request, pk):
    comment = Comment.objects.get(pk=pk)
    data = CommentSerializer(instance=comment, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_comments(request, pk):
    comment = get_object_or_404(comment, pk=pk)
    comment.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
