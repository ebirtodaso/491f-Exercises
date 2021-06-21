from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('list/', include('list.urls')),
    path('admin/', admin.site.urls),
]
