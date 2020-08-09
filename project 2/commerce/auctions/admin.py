from django.contrib import admin
from .models import Bid, Comment, Listing, User, Watchlist

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(Watchlist)
