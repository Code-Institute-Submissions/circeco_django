from django.shortcuts import render, redirect, reverse
from .models import UserFavouriteShop
from shops.models import Shop


# Create your views here.
def view_fav(request):
    """A View that renders the fav contents page"""
    favs = UserFavouriteShop.objects.all().filter(user = request.user)
    return render(request, "fav.html", {"fav_items": favs})


def add_to_fav(request, shopId):
    """xxx"""

    userId = request.user
    # TODO associate userId and shopId

    print(shopId, userId)

    shop = Shop.objects.get(id=shopId)
    newFav = UserFavouriteShop(user=userId, shop=shop)
    newFav.save()

    print(newFav.id)

    return redirect(reverse('view_fav'))


def remove_fav(request, shopId):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))