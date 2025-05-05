from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from country_api.views import CountryListView, CountryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('country_api.urls')),
    path('', CountryListView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailView.as_view(), name='country_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]