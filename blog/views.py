from django.shortcuts import render,redirect
from .forms import  PostForm
from django.contrib import messages
from .models import Post,Comment
from django.views.generic import CreateView
from django.urls import reverse_lazy


def new_post(request):

    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            new_creator=form.save(commit=False)
            new_creator.author =request.user
            new_creator.save()
            form.save_m2m()
            return redirect("home")

    context = {"form": form}

    return render(request, "blog/newpost.html", context)

def post_list(request):
    posts = Post.objects.all()

    context = {"posts": posts}
    

    return render(request, "user/home.html", context)



#içeride olan veriyi istediğimiz verimi degil mi diye eşleştirmek için id kullanıyoruz
#Yani id ye göre veri çektik
def post_update(request, id):
#todo değişkenine id si benim yazdığım id ile aynı olan varsa databasede onu atadık
    post = Post.objects.get(id=id)
#form değişkeninin içini todo ile doldurduk instance kalıp
    form = PostForm(instance=post)

    if request.method == "POST":
#request.POSTtan gelen veri ile instance yani databasedeki verimi karşılaştırıyor değişen bir yer varsa
# değiştiriyor tek bir veri haline getiriyor  
        form = PostForm(request.POST, instance=post)
#validasyonu yaptık yani fieldlar uygun mu gibi seyler
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"post": post, "form": form}

    return render(request, "blog/post_update.html", context)



def post_delete(request, id):
    post = Post.objects.get(id=id)

    if request.method == "POST":
        post.delete()
        return redirect("home")

    context = {"post": post}
    return render(request, "blog/post_delete.html", context)


def post_detail(request,id):
    post=Post.objects.get(id=id)
    
    context={"post":post}
    return render(request,"blog/post_detail.html" ,context)






class AddCommentVİew(CreateView):
    model =Comment
    template_name ="blog/add_comment.html"
    fields ="__all__"
    #form_class = CommentForm
    success_url = reverse_lazy('home')


