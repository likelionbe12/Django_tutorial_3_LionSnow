from django.urls import path
from . import views

app_name='imageapp'

urlpatterns = [   
    # 카테고리 관리
    path('', views.index, name='index'), 
    path('image/write/', views.image_write, name="image_write"),
    path('image/<int:image_id>', views.image_detail, name='image_detail'),
    path('image/<int:image_id>/edit/', views.image_edit, name='image_edit'), # 이미지 편집(update)
    path('image/<int:image_id>/delete/', views.image_delete, name='image_delete'),
    # 구독
    path('image/<int:image_id>/toggle_subscribe', views.toggle_subscribe, name='toggle_subscribe')
]