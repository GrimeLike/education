from django.urls import path, include
from rest_framework import routers

from courses.api.views import *

app_name = 'courses'

router = routers.DefaultRouter()
router.register('courses', CourseViewSet)

urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjects/<pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('', include(router.urls)),
]
