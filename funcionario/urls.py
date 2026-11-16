from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('', RedirectView.as_view(pattern_name='lista_funcionarios', permanent=False)),
]
