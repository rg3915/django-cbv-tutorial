from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url as r
from django.test import TestCase

from pocket.financial.models import Expense


class TestExpense(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'regis@email',
            'lorem'
        )
        self.client.force_login(self.user)
        self.expense = Expense.objects.create(
            description='lorem',
            value=1
        )

    def test_context(self):
        response = self.client.get(r('financial:expense_list'))
        self.assertEqual(response.context['verbose_name'], 'Despesa')
        self.assertEqual(response.context['verbose_name_plural'], 'Despesas')
        self.assertEqual(response.context['total'], 1)
