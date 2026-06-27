from django.contrib import admin 
from django.urls import include, path 
#from .views import sayHello 
from restaurant import views
#from rest_framework import routers

#router = routers.DefaultRouter()

#router.register(r'users', views.UserViewSet)
  
urlpatterns = [ 
   
    #path('', views.index, name='index'),
    #path('admin/', admin.site.urls),
   # path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('menu/', views.MenuItemsView.as_view()),
    #path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    #path('menu/items', views.MenuItemsView.as_view()),
    #path('menu/items/<int:pk>', views.SingleMenuItemView.as_view()),
    
    path('menu/items/', views.MenuItemsView.as_view()),
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view()),
]

