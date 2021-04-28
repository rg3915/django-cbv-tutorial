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
from .mixins import (
    ExpenseContextDataMixin,
    ExpenseFormKwargsMixin,
    SearchMixin
)
from .models import Expense


class ExpenseListView(LRM, ExpenseContextDataMixin, SearchMixin, ListView):
    model = Expense
    # context_object_name = 'expense_list'
    # paginate_by = 10
    # template_name = 'expense_list.html'

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         message = 'Você não tem permissão para acessar essa página.'
    #         messages.error(request, message)
    #         return redirect('core:index')
    #     return super(ExpenseListView, self).dispatch(request, *args, **kwargs)


class ExpenseNotPaidListView(ExpenseContextDataMixin, SearchMixin, ListView):
    model = Expense

    def get_queryset(self):
        return Expense.objects.filter(paid=False)


class ExpenseDetailView(DetailView):
    model = Expense


class ExpenseCreateView(ExpenseFormKwargsMixin, CreateView):
    model = Expense
    form_class = ExpenseForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # user = self.request.user
        person = Person.objects.get(first_name='Huguinho')
        context['huguinho_expenses'] = Expense.objects.filter(person=person)
        return context

    def post(self, request, *args, **kwargs):
        print('>>> POST')
        # Serve pra debugar o código e pegar os valores do formulário.
        # request.POST
        # request.FILES
        # form = self.get_form()
        # form.is_valid()
        # form.errors
        # Exemplificar isso aqui.
        form = super().post(request, *args, **kwargs)
        return form

    def get_form_class(self):
        if self.request.user.is_authenticated:
            return ExpenseEditForm
        return ExpenseForm

    def form_valid(self, form):
        # form.send_email()
        print('Enviar email')
        return super(ExpenseCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('financial:expense_list')


class ExpenseUpdateView(ExpenseFormKwargsMixin, UpdateView):
    model = Expense
    form_class = ExpenseEditForm


class ExpenseDeleteView(DeleteView):
    model = Expense
    success_url = reverse_lazy('expense:expense_list')
