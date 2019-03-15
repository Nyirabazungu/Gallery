from django.shortcuts import render
from . models import Image,Category

# Create your views here.
def welcome(request):
    pictures = Image.objects.all()
    return render(request, 'welcome.html',{"pictures":pictures})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})


def category(request,category_id):
    try:
        category = Category.objects.get(id = category_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/category.html", {"category":category}) 






