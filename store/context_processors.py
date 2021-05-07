from .models import Category


def categories(request):
    """To make available in all views, add 'store.views.categories' to TEMPLPATES.OPTIONS.context_processors"""
    return {
        'categories': Category.objects.all()
    }