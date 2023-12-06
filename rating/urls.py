from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import Mealviewset,Ratingviewset

router=routers.DefaultRouter()
router.register('mealsapi',Mealviewset)
router.register('rateapi',Ratingviewset)

urlpatterns = [
    path('',include(router.urls)),

]
