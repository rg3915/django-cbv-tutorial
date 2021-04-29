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
