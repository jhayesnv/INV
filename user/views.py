from datetime import date, timedelta

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from event.models import (
    Event,
    Reservation
)

from inventory.models import (
    SpiritOrderItem,
    WineOrderItem,
    BeerOrderItem,
    Update
)

from recipe.models import MenuItemRecipe


def get_well_pours():
    well_pours = SpiritOrderItem.objects.filter(Q(is_well=True),
                                                Q(is_active=True))
    return well_pours


def get_glass_pours():
    glass_pours = WineOrderItem.objects.filter(Q(is_glass_pour=True),
                                               Q(is_active=True))
    return glass_pours


def get_draft_pours():
    draft_pours = BeerOrderItem.objects.filter(Q(format='Draft'),
                                               Q(is_active=True))
    return draft_pours


def get_events():
    startdate = date.today()
    enddate = startdate + timedelta(days=13)
    events = Event.objects.filter(
        date__range=[startdate, enddate]).order_by('date')

    return events


def get_reservations():
    startdate = date.today()
    enddate = startdate + timedelta(days=6)
    reservations = Reservation.objects.filter(
        date__range=[startdate, enddate]).order_by('date')

    return reservations


def get_updates():
    startdate = date.today()
    enddate = startdate - timedelta(days=30)
    updates = Update.objects.filter(
        submitted__range=[enddate, startdate]).order_by('submitted')

    return updates


def get_out_of_stock_items():
    spirits = SpiritOrderItem.objects.filter(is_available=False)
    wine = WineOrderItem.objects.filter(is_available=False)
    beer = BeerOrderItem.objects.filter(is_available=False)
    food = MenuItemRecipe.objects.filter(is_available=False)

    aggregate_items = {
        'spirits': spirits,
        'wine': wine,
        'beer': beer,
        'food': food
    }

    return aggregate_items


@login_required(login_url='/accounts/login/')
def user_home_view(request):
    context = {
        'well_pours': get_well_pours(),
        'glass_pours': get_glass_pours(),
        'draft_pours': get_draft_pours(),
        'out_of_stock_items': get_out_of_stock_items(),
        'events': get_events(),
        'reservations': get_reservations(),
        'updates': get_updates()
    }

    return render(request, 'user/home.html', context)
