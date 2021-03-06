from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from packages.models import Package


def view_bag(request):
    """ A view to render bag content """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ To add package to the bag """

    package = get_object_or_404(Package, pk=item_id)
    # package = request.POST.get('package')
    # quantity = request.POST.get('quantity')
    # redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if not bag.keys():
        bag[item_id] = {}
        messages.success(
            request, f'Added {package.friendly_name} Logo Package to your bag')
    else:
        messages.error(
            request, "You already have an item in the bag and can only order one \
                 at a time. Please edit your bag or if details are good,\
                      proceed to purchase. ")
        return redirect('view_bag')

    # if item_id in list(bag.keys()):
    #     bag[item_id] += quantity
    #     messages.success(
    #         request, f'Added {package.friendly_name} Logo Package to your bag')
    # else:
    #     bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect('view_bag')
