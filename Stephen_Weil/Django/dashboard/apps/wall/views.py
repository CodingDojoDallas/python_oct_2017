from django.shortcuts import render, redirect
from .models import *
from ..users.models import *
from django.contrib import messages

def index(req, userid):
    if 'id' not in req.session:
        return redirect('/signin')
    user = User.objects.get(id=userid)
    context = {
        'user': user,
        'posts': Post.objects.filter(recipient=user)
    }
    replies = []
    for post in context['posts']:
        found = Reply.objects.filter(message=post)
        if found.exists():
            replies += list(found)
    context['replies'] = replies
    return render(req, 'wall/index.html', context)

def post(req, userid):
    if 'id' not in req.session:
        return redirect('/signin')
    if req.method == "POST":
        d = req.POST
        errors = Post.objects.validator(d, userid)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(req, error, extra_tags=tag)
        else:
            sender = req.session['id']
            Post.objects.create_post(sender, d, userid)
    url = '/users/show/' + userid
    return redirect(url)

def reply(req, userid, postid):
    if 'id' not in req.session:
        return redirect('/signin')
    if req.method == "POST":
        d = req.POST
        errors = Reply.objects.reply_validator(d, postid)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(req, error, extra_tags=tag)
        else:
            sender = req.session['id']
            Reply.objects.create_reply(sender, d, postid)
    url = '/users/show/' + userid
    return redirect(url)