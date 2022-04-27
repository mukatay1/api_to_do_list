from django.contrib import admin
from .models import UserProfile, Current


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname', 'photo')
    search_fields = ('user', 'name')


@admin.register(Current)
class CurrentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'parent', 'author', 'is_completed')
    list_filter = ('is_completed',)
    fieldsets = (
        ('Общая информация', {
            'fields': ('title', 'parent', 'author', 'is_completed')
        }),
        ('Таблица времени',
         {'fields': ('start', 'end'),
          'description': 'Две точки времени для определения промежутка',
          })
    )
