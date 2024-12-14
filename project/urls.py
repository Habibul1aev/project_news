from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('detal/<int:id>', views.detal_news, name='detal_news'),
    path('category/<int:id>', views.categorys, name='categorys')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

