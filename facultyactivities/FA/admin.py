from django.contrib import admin
from .models import AdminLogin,FacultyLogin,SDP_attended

# Register your models here.
admin.site.register(AdminLogin)
admin.site.register(FacultyLogin)
admin.site.register(SDP_attended)