from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', views.add.as_view(), name='create'),
    path('update/<int:id>/', views.Update.as_view(), name='update'),
    path('delete/<int:id>/', views.Delete.as_view(), name='delete'),
]

# Optional: Serve static files during development

