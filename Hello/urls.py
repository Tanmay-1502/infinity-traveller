from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "AMAZON Admin"
admin.site.site_title = "AMAZON Admin Portal"
admin.site.index_title = "Welcome to AMAZON Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))

]
