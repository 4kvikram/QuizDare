from django.contrib import admin
from .models import Register,Questions,UserAnswer,FriendsAnswer
# Register your models here.
admin.site.register(Register)
admin.site.register(Questions)
admin.site.register(UserAnswer)
admin.site.register(FriendsAnswer)
