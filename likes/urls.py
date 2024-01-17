from django.urls import path
from .views import AddLike,AddDislike


urlpatterns = [
    path('<int:pk>/like/', AddLike.as_view(), name='like'),
    path('<int:pk>/dislike/', AddDislike.as_view(), name='dislike')
]