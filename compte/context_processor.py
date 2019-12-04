from .models import *


def utilsproc(request):
    if request.user.is_authenticated:
        abonnes = request.user.profile.abonnes.all()
        abonnements = request.user.abonnements.all()
        suggestions = Profile.objects.difference(request.user.abonnements.all())
        notebox = NotificationBox.objects.get(user=request.user)
    return locals()