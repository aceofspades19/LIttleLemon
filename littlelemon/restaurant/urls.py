from django.urls import path, include
from restaurant import views
from rest_framework.routers import DefaultRouter 


router = DefaultRouter(trailing_slash=False)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('', views.index, name='index'),
    path('', views.index, name='home'),
    path('booking/', include(router.urls)) 
]

