# Generated by Django 5.0.6 on 2024-05-30 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asdavi', '0003_aluno_autorizacao_aluno_interesse_educacional_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='autorizacao',
        ),
    ]
