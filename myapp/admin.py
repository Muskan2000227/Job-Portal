from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(register_user)
admin.site.register(register_emp)
admin.site.register(Jobs)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Resume)
admin.site.register(Saved)
admin.site.register(ResumeBuilder)
