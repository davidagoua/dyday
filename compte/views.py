from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from .forms import UserCreationForm, ProfileCreationForm, LoginForm
from django.contrib.auth import login, logout, authenticate, mixins
from .models import Profile, User, NotificationBox, Notification
from blog.models import SimplePost


class WelcomeView(generic.TemplateView):
    template_name = 'welcome.html'


class InscriptionView(View):
    template_name = 'compte/inscription.html'
    form = UserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        print("Entrez: InscriptionView::post")
        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            profile = Profile.objects.create(user=user)
            NotificationBox.objects.create(user=user).save()
            profile.save()
            login(request, user)
            return redirect('compte:profile', profile.slug)
        return render(request, self.template_name, locals())


class HomeView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'home.html'
    login_url = 'welcome'

    def get_context_data(self, **kwargs):
        data = super(HomeView, self).get_context_data(**kwargs)
        data['postes'] = SimplePost.objects.all()
        return data


class ProfileView(mixins.LoginRequiredMixin, generic.DetailView):
    login_url = 'welcome'
    model = Profile
    context_object_name = 'profile'
    template_name = 'compte/profile.html'

    def get_context_data(self, **kwargs):
        data = super(ProfileView, self).get_context_data(**kwargs)
        data['update_form'] = ProfileCreationForm
        data['update_form'].instance = self.get_object()
        return data

    @staticmethod
    def update_profile(request, slug,  *args, **kwargs):
        form = ProfileCreationForm(request.POST, request.FILES)
        profile = get_object_or_404(Profile, slug=slug)
        if form.is_valid():
            profile.contact = form.cleaned_data['contact']
            profile.info = form.cleaned_data['info']
            profile.avatar = form.cleaned_data['avatar']
            profile.address = form.cleaned_data['address']
            profile.save()
        return redirect('compte:profile', profile.slug)


def deconnection(request):
    logout(request)
    return redirect('welcome')

def connection(request):
    error = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('home')
            else: error = True
    else:
        form = LoginForm
    return render(request, 'compte/login.html', locals())

def suivre(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.abonnes.add(request.user)
    notext = f"{request.user.username.title()} à commencer a suivre {profile.user.username}"
    note = Notification(text=notext)
    note.save()
    request.user.notebox.notifications.add(note)
    profile.user.notebox.notifications.add(note)
    next = request.GET['next'] if 'next' in request.GET else 'home'
    return redirect(next)

def abandonner(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.abonnes.remove(request.user)
    next = request.GET['next'] if 'next' in request.GET else 'home'
    return redirect(next)


class ProfileListView(generic.ListView):
    template_name = 'compte/profile_list.html'
    model = Profile
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.difference(self.request.user.abonnements.all())


class NoteListView(generic.ListView):
    template_name = 'compte/note_list.html'
    model = Notification
    queryset = Notification.objects.all()
    context_object_name = 'notes'

    def get_queryset(self):
        queryset = super(NoteListView, self).get_queryset()
        for profile in self.request.user.abonnements.all():
            queryset.union(queryset, profile.user.notebox.notifications.all()).order_by('-time')

        return queryset
