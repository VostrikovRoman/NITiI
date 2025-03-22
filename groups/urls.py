from django.urls import path
from . import views

urlpatterns = [
    path('', views.groups, name='groups'),
    path('add', views.add, name='add_group'),
    path('<int:pk>', views.Group_Page.as_view(), name='group_page'),
    path('<int:pk>/delete', views.Delete.as_view(), name='group_delete'),
    path('<int:pk>/update', views.Update.as_view(), name='group_update')
]