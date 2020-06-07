from django import template
register = template.Library()

@register.simple_tag
def difference(pc1_price, pc2_price, option):
    mayor = pc1_price if  pc1_price > pc2_price else pc2_price
    menor = pc2_price if  pc1_price > pc2_price else pc1_price

    if option == 1:
        dif = mayor - menor
        return "{:,}".format(dif)
    elif option == 2:
        porcen = (menor*100) / mayor
        return round(100-porcen, 1)
    
