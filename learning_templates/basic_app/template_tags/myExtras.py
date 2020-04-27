#hot to create own filters
#1. register all of this

from django import template
register=template.Library()

def dum(value,arg):
    """
    this cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')

register.filter('cut',dum)
