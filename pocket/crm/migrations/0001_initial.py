# Generated by Django 3.2 on 2021-04-27 21:17

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='endereço')),
                ('address_number', models.IntegerField(blank=True, null=True, verbose_name='número')),
                ('complement', models.CharField(blank=True, max_length=100, null=True, verbose_name='complemento')),
                ('district', models.CharField(blank=True, max_length=100, null=True, verbose_name='bairro')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='cidade')),
                ('uf', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, null=True, verbose_name='UF')),
                ('cep', models.CharField(blank=True, max_length=9, null=True, verbose_name='CEP')),
                ('country', models.CharField(blank=True, default='Brasil', max_length=50, null=True, verbose_name='país')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=11, null=True, verbose_name='RG')),
                ('cnh', models.CharField(blank=True, max_length=20, null=True, verbose_name='CNH')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('exist_deleted', models.BooleanField(default=True, help_text='Se for True o item existe. Se for False o item foi deletado.', verbose_name='existe/deletado')),
                ('first_name', models.CharField(max_length=50, verbose_name='nome')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='sobrenome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'pessoa',
                'verbose_name_plural': 'pessoas',
                'ordering': ('first_name',),
            },
        ),
    ]