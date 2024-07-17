from django.contrib import admin
from .models import Actor,Movies

# Register your models here.


class AdminActor(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ('name', 'age')
    list_filter = ('name', 'age')
    list_per_page = 2
    # list_display_links = None
    # list_editable = ('name', 'age')
    ordering = ['age']


admin.site.register(Actor, AdminActor)


class AdminMovies(admin.ModelAdmin):
    list_display = ('id', 'title', 'actor_name', 'actor_age')

    def actor_name(self, obj):
        return obj.actor.name

    def actor_age(self, obj):
        return obj.actor.age

admin.site.register(Movies, AdminMovies)