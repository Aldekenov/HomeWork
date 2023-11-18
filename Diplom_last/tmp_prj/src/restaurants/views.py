from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages

from src.restaurants.models import Restaurant, Review
from src.profiles.models import Profile
from src.restaurants.utils import divide_chunks


def get_sort_by(sort_by_val):
    if sort_by_val == "created_at_desc":
        return "-id"
    elif sort_by_val == "created_at_asc":
        return "id"
    elif sort_by_val == "rating_desc":
        return "-rating"
    elif sort_by_val == "rating_asc":
        return "rating"
    elif sort_by_val == "name_desc":
        return "-name"
    elif sort_by_val == "name_asc":
        return "name"
    return "-rating"


def main(request):
    if request.method == "GET":
        template = loader.get_template("pages/main.html")
        sort_by_val = request.GET.get("sort_by")
        sort_by = get_sort_by(sort_by_val)
        restaurants = Restaurant.objects.order_by(sort_by)
        paginator = Paginator(restaurants, 20)
        page_number = request.GET.get("page", 1)
        page_restaurants = paginator.get_page(page_number)
        restaurants_chunks = divide_chunks(page_restaurants, size=4)
        context = {
            "page_restaurants": page_restaurants,
            "restaurants_chunks": restaurants_chunks,
        }
        return HttpResponse(template.render(context, request))
    return redirect("main")


def restaurants_detail_view(request, restaurant_id):
    if request.method == "GET":
        template = loader.get_template("pages/restaurants_detail.html")
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        reviews = Review.objects.filter(restaurant_id=restaurant_id).order_by("-id")
        context = {"restaurant": restaurant, "reviews": reviews}
        return HttpResponse(template.render(context, request))
    return redirect("main")


def reviews_view(request):
    if request.method == "POST":
        restaurant_id = request.POST.get("restaurant_id")
        user_id = request.user.id
        text = request.POST.get("text")
        short_review = request.POST.get("short_review")
        rating = request.POST.get("rating")
        Review.objects.create(
            restaurant_id=restaurant_id,
            user_id=user_id,
            text=text,
            short_review=short_review,
            rating=rating,
        )
        messages.success(request, "You have successfully added a review")
        return redirect("restaurants-detail", restaurant_id=restaurant_id)
    return redirect("main")


def about_view(request):
    if request.method == "GET":
        template = loader.get_template("pages/about.html")
        return HttpResponse(template.render({}, request))