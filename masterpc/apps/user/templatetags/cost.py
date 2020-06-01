from django import template
register = template.Library()

@register.filter
def cost(pc):
    total = 0
    if pc.cpu.first(): total += pc.cpu.first().price
    if pc.gpu.first(): total += pc.gpu.first().price
    if pc.board.first(): total += pc.board.first().price
    if pc.ram.first(): total += pc.ram.first().price
    if pc.psu.first(): total += pc.psu.first().price
    if pc.case.first(): total += pc.case.first().price

    for s in pc.storage.all():
        total += s.price

    return total