from django.urls import path

from pocket.financial import views as v

app_name = 'financial'

urlpatterns = [
    path('', v.ExpenseListView.as_view(), name='expense_list'),
    path('not-paid/', v.ExpenseNotPaidListView.as_view(), name='expense_not_paid_list'),  # noqa E501
    path('<int:pk>/', v.ExpenseDetailView.as_view(), name='expense_detail'),
    path('create/', v.ExpenseCreateView.as_view(), name='expense_create'),
    path('<int:pk>/update/', v.ExpenseUpdateView.as_view(), name='expense_update'),
    path('<int:pk>/delete/', v.ExpenseDeleteView.as_view(), name='expense_delete'),
]
