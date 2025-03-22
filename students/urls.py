from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('add', views.add, name='add_student'),
    path('<int:pk>', views.Student_Page.as_view(), name='student_page'),
    path('<int:pk>/update', views.Update.as_view(), name='student_update'),
    path('<int:pk>/delete', views.Delete.as_view(), name='student_delete'),
]
