from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View

from pocket.financial.models import Expense

# class IndexView(View):

#     def get(self, request):
#         template_name = 'index.html'
#         expense_list = Expense.objects.all()
#         context = {'expense_list': expense_list}
#         return render(request, template_name, context)


# class IndexView(TemplateView):
#     model = Expense  # na verdade isso aqui não tem utilidade
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         expense_list = Expense.objects.all()
#         context = {'expense_list': expense_list}
#         return context


class IndexView(ListView):
    model = Expense
    template_name = 'index.html'
    context_object_name = 'expense_list'
