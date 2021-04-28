from django.urls import path

from pocket.crm import views as v

app_name = 'crm'


urlpatterns = [
    path('', v.PersonListView.as_view(), name='person_list'),
    path('<int:pk>/', v.PersonDetailView.as_view(), name='person_detail'),
    path('create/', v.PersonCreateView.as_view(), name='person_create'),
    path('<int:pk>/update/', v.PersonUpdateView.as_view(), name='person_update'),
    path('<int:pk>/delete/', v.PersonDeleteView.as_view(), name='person_delete'),
]
