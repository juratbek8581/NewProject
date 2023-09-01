from django.urls import path 
 


from .views import HomePageView , AboutPageView, TelegramPageView, InstagramPageView


urlpatterns = [
    path('about/',AboutPageView.as_view(), name = 'about'),
    path('',HomePageView.as_view(),name = 'home'),
    path('telegram/', TelegramPageView.as_view(), name = 'telegram'),
    path('instagram/', InstagramPageView.as_view(), name = 'instagram'),
]