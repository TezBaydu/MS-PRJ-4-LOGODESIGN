from django.shortcuts import render


def view_bag(request):
    """ A view to render bag content """

    return render(request, 'bag/bag.html')
