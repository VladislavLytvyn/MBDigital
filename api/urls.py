from django.urls import include, path

from api.views import PersonList, PersonDetail, GroupList, GroupDetail


urlpatterns = [
    path('', include('rest_framework.urls')),
    path('persons/', PersonList.as_view(), name='persons'),
    path('persons/<int:pk>/', PersonDetail.as_view(), name='person_detail'),
    path('groups/', GroupList.as_view(), name='groups'),
    path('groups/<int:pk>/', GroupDetail.as_view(), name='group_detail'),
]
