from django.contrib import admin
from .models import User_details, Project, UserSkills, PositionModel, Applications

# Register your models here.


admin.site.register(User_details)
admin.site.register(Project)
admin.site.register(UserSkills)
admin.site.register(PositionModel)
admin.site.register(Applications)
