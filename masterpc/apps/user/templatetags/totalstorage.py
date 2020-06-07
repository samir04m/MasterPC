from django import template
register = template.Library()

@register.simple_tag
def totalstorage(pc1, pc2, option):
    total1 = 0
    total2 = 0

    for s in pc1.storage.all():
        total1 += s.price

    for s in pc2.storage.all():
        total2 += s.price

    mayor = total1 if  total1 > total2 else total2
    menor = total2 if  total1 > total2 else total1

    if option == 1:
       return "{:,}".format(total1)
    elif option == 2:
        return "{:,}".format(total2)
    elif option == 3:
        dif = mayor - menor
        return "{:,}".format(dif)
    elif option == 4:
        porcen = (menor*100) / mayor
        return round(100-porcen, 1)
        