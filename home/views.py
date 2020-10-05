from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.models import Friends, Create_Post
from home.forms import AddFriendForm, UserUpdateForm, Post_form



@login_required
def home(request):
    post_message = Post_form()
    all_posts = Create_Post.objects.all().order_by('-posted_time')
    if request.method=='POST':
        post_message=Post_form(request.POST or None)
        if post_message.is_valid():
            fs=post_message.save(commit=False)
            fs.posted_by= request.user
            fs.save()
            post_message.save()
            post_message = Post_form()
            return render(request,'home/index.html', {'post':post_message, 'all_posts':all_posts})

            
    return render(request,'home/index.html', {'post':post_message, 'all_posts':all_posts})

@login_required
def friends(request):
    friends_list = Friends.objects.all() # its common error
    return render(request, 'home/friends.html', {'friends_list':friends_list,})

@login_required()
def add_friend(request):
    form = AddFriendForm() # refresh the form
    if request.method=='POST':
        form = AddFriendForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = UserUpdateForm(None)

    return render(request, 'home/add_friend.html', {'a_form':form}) 

@login_required()
def del_friend(request,id):
    friend_by_id = Friends.objects.get(id=id)
    friend_by_id.delete()
    return redirect('/friends')

@login_required()
def update_friend(request, id):
    frid = Friends.objects.get(id=id)
    if request.method=='POST':
        form = UserUpdateForm(request.POST, instance=frid)
        if form.is_valid():
            form.save()
            #form = UserUpdateForm(None)
        return redirect('/friends')
    return render(request, 'home/update_friend.html', {'f':frid})

