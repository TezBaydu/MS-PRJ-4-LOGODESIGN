from django.shortcuts import render
from .models import Company, Project, Package


def all_projects(request):
    """ A view to show Case Studies including filtering """

    projects = Project.objects.all()
    companies = None

    if request.GET:
        if 'company' in request.GET:
            companies = request.GET['company']
            projects = projects.filter(company__name=companies)
            company = Company.objects.filter(name=companies)[0]

    context = {
        'projects': projects,
        'company': company,
    }

    return render(request, 'packages/packages.html', context)


def all_packages(request):
    """ A view to show all packages """

    packages = Package.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)
