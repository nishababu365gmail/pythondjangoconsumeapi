from django import template
register = template.Library()

def Expand(value): # Only one argument.
    """Converts a string into all lowercase"""
    
    
    if value==True:
     return 'Single'
    else:
     return 'Bunch'
register.filter('expand', Expand)

