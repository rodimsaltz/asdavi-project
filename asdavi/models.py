from django.db import models

# Create your models here.
class Aluno(models.Model):

    nome_aluno = models.CharField(max_length=64, null = False, blank= False)

    data_nascimento = models.DateField(null = False , blank = False)

    genero_aluno = models.CharField(max_length=10, null = False, blank= False)

    documento_aluno = models.CharField(max_length=64, null = False, blank= False)

    endereco_aluno = models.CharField(max_length=64, null = False, blank= False)

    telefone_aluno = models.CharField(max_length=64, null = False, blank= False)

    nome_enfermidade = models.CharField(max_length=64, null = True, blank= True)

    nome_medicamento = models.CharField(max_length=64, null = True, blank= True)

    renda_familiar = models.IntegerField(null = False, blank = False)

    condicoes_familiar = models.CharField(max_length=50, null = False, blank = False)

    interesse_educacional = models.CharField(max_length=50)

    necessidade_especial = models.CharField(max_length=64)

    def __str__(self):
        return self.nome_aluno
    
    
