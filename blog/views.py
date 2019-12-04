from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic
from .models import *
from .forms import *


class ActualfilView(View):

    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, locals())


def liker(request, pk, **kwargs):
    poste = get_object_or_404(SimplePost, pk=pk)
    if request.user not in poste.likers.all():
        poste.likers.add(request.user)
    else:
        poste.likers.remove(request.user)
    return JsonResponse({'likes': poste.likers.count()})

def post(request, *args, **kwargs):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        form.instance.user = request.user
        post = form.save()
        post.save()
    return redirect('home')