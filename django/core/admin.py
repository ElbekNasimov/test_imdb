from django.contrib import admin
from .models import Movie, Vote, MovieImage, Person, Role


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'year', 'rating', 'runtime', 'website', 'get_actors', 'get_writers')
    search_fields = ('title', 'plot')
    list_filter = ('rating', )
    list_per_page = 25

    def get_actors(self, obj):
        return "\n".join([act.first_name for act in obj.actors.all()])

    def get_writers(self, obj):
        return "\n".join([writer.first_name for writer in obj.writers.all()])


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'value')


@admin.register(MovieImage)
class MovieImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'movie', 'user')


admin.site.register(Person)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('movie', 'person', 'name')
