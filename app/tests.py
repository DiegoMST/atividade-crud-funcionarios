from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from .models import Funcionario

class FuncionarioCRUDTests(TestCase):
    def setUp(self):
        self.funcionario = Funcionario.objects.create(
            nome='Funcionário Teste', cpf='123.456.789-00',
            email='teste@example.com', remuneracao=Decimal('3000.00'),
        )

    def test_listagem_e_detalhes(self):
        self.assertContains(self.client.get(reverse('lista_funcionarios')), 'Funcionário Teste')
        self.assertContains(self.client.get(reverse('listar_funcionario', args=[self.funcionario.pk])), '3000')

    def test_cadastro(self):
        response = self.client.post(reverse('form_funcionario'), {
            'nome': 'Novo Nome', 'cpf': '987.654.321-00',
            'email': 'novo@example.com', 'remuneracao': '4200.00',
        })
        self.assertRedirects(response, reverse('lista_funcionarios'))
        self.assertTrue(Funcionario.objects.filter(nome='Novo Nome').exists())

    def test_edicao(self):
        response = self.client.post(reverse('editar_funcionario', args=[self.funcionario.pk]), {
            'nome': 'Nome Editado', 'cpf': '123.456.789-00',
            'email': 'teste@example.com', 'remuneracao': '3200.00',
        })
        self.assertRedirects(response, reverse('lista_funcionarios'))
        self.funcionario.refresh_from_db()
        self.assertEqual(self.funcionario.nome, 'Nome Editado')

    def test_exclusao_exige_confirmacao_post(self):
        url = reverse('remover_funcionario', args=[self.funcionario.pk])
        self.client.get(url)
        self.assertTrue(Funcionario.objects.filter(pk=self.funcionario.pk).exists())
        self.assertRedirects(self.client.post(url), reverse('lista_funcionarios'))
        self.assertFalse(Funcionario.objects.filter(pk=self.funcionario.pk).exists())
