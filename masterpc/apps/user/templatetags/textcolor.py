from django import template
register = template.Library()

@register.filter
def textcolor(pc_view, a_view):
    if pc_view == a_view:
        return 'text-warning'
    else:
        return 'text-light'
        