from django import template
from .models import Profile

register = template.Library()


def commonab(value, arg):
    pass


register.filter('commonab', commonab)
