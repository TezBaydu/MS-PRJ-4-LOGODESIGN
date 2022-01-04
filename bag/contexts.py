from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from packages.models import Package


def bag_contents(request):

    bag_items = []
    grand_total = 0
    bag = request.session.get('bag', {})

    for item_id in bag.items():
        package = get_object_or_404(Package, pk=item_id)
        bag_items.append({
            'item_id': item_id,
            'package': package,
            'package.price': package.price,
            'package.name': package.name,
            'package.friendly_name': package.friendly_name,
            'package.logo_count_request': package.logo_count_request,
            'package.quality_request': package.quality_request,
            'package.support_request': package.support_request,
            'package.production_days': package.production_days,
        })

    # grand_total += package.price

    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
    }

    return context
