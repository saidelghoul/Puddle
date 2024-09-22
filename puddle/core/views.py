from django.shortcuts import render

from item.models import Category, Item


def index(req):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(
        req,
        "core/index.html",
        {
            "categries": categories,
            "items": items,
        },
    )


def contact(req):
    return render(req, "core/contact.html")
