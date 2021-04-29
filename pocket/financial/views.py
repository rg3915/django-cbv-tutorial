from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from pocket.crm.models import Person

from .forms import ExpenseEditForm, ExpenseForm
# from .mixins import (
#     ExpenseContextDataMixin,
#     ExpenseFormKwargsMixin,
#     SearchMixin
# )
from .models import Expense


class ExpenseListView(ListView):
    model = Expense
    # context_object_name = 'expense_list'
    # paginate_by = 10
    # template_name = 'expense_list.html'


class ExpenseNotPaidListView(ListView):
    model = Expense

    def get_queryset(self):
        return Expense.objects.filter(paid=False)


class ExpenseDetailView(DetailView):
    model = Expense


class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm


class ExpenseUpdateView(UpdateView):
    model = Expense
    form_class = ExpenseEditForm


class ExpenseDeleteView(DeleteView):
    model = Expense
    success_url = reverse_lazy('expense:expense_list')
