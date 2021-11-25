from pages.models import Page

def get_pages(request):

    pages = Page.objects.filter(hidden=True).order_by('order').values_list('id', 'title', 'slug')

    return {
        'pages': pages
    }