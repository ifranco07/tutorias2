# urls.py
from django.urls import path
from .views import create_professor, reactivate_interview, register, register_admin, students_list

urlpatterns = [
    path('register/', register, name='register'),
    path('students/', students_list, name='students_list'),
    path('reactivate_interview/<int:student_id>/', reactivate_interview, name='reactivate_interview'),
    path('create_p/', create_professor, name='create_professor'),
    path('register_admin/', register_admin, name='register_admin'),
    # otras rutas
]
