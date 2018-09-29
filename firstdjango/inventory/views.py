from django.shortcuts import render
from django.http import Http404

from inventory.models import Item

'''
show title of all items
that are in stock
'''
def index(request):
    items = Item.objects.exclude(amount=0)

    #render creates a response for us and also wire view to a template
    return render(request,'inventory/index.html',{
        'items':items,
    })


'''
write detail for a particular item
'''
def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('This item does not exist')

    return (render,'inventory/item_detail.html',{
        'item':item,
    })

