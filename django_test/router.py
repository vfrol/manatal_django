from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter


from schools.views import SchoolViewSet
from students.views import StudentViewSet


router = DefaultRouter(trailing_slash=True)
router.register('schools', SchoolViewSet, basename='school')
router.register('students', StudentViewSet, basename='student')

students_router = NestedDefaultRouter(router, 'schools', lookup='school')
students_router.register('students', StudentViewSet, basename='school_students')


urlpatterns = []
urlpatterns += router.urls
urlpatterns += students_router.urls