from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Options)
admin.site.register(question_wise_result)
admin.site.register(category_wise_result)
admin.site.register(User)

