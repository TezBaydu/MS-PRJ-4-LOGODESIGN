from django.shortcuts import render, get_object_or_404
from .models import Company, Project, Package


def projects_packages(request):
    """ A view to show Case Studies including filtering and all packages """

    projects = Project.objects.all()
    packages = Package.objects.all()
    companies = None

    if request.GET:
        if 'company' in request.GET:
            companies = request.GET['company']
            projects = projects.filter(company__name=companies)
            company = Company.objects.filter(name=companies)[0]

    context = {
        'projects': projects,
        'company': company,
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)


def package_detail(request, package_id):
    """ A view to show individual package details """

    package = get_object_or_404(Package, pk=package_id)

    context = {
        'package': package,
    }

    return render(request, 'packages/checkout.html', context)