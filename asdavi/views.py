from django.shortcuts import render


from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from asdavi.models import Aluno
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.models import User

class IndexTemplateView(TemplateView):
    template_name = "index.html"

class PagamentoTemplateView(TemplateView):
    template_name = "pagamento.html"
    
class DoacaoTemplateView(TemplateView):
    template_name = "doacao.html"   

class LoginTemplateView(TemplateView):
    template_name = "login.html"

class CadastroCreateView(CreateView):
    template_name = "cadastro.html"
    model = Aluno
    fields = ['nome_aluno', 'data_nascimento', 'genero_aluno', 'documento_aluno', 'endereco_aluno', 'telefone_aluno', 'nome_enfermidade', 'nome_medicamento', 'renda_familiar', 'condicoes_familiar', 'interesse_educacional', 'necessidade_especial' ]
    def get_success_url(self):
        return reverse_lazy('index')
    
class PesquisaAlunoView(ListView):
    model = Aluno
    template_name = "lista_alunos.html"
    context_object_name = 'aluno'

class EditarAlunoView(DetailView):
    model = Aluno
    template_name = "editar.html"
    def get_success_url(self):
        return redirect('alunos')
    
def Excluir_Aluno(request, pk): # FUNÇÃO PARA EXCLUIR ALUNO
    aluno = get_object_or_404(Aluno, pk=pk) # PEGANDO O PK DO ALUNO PELO FOR DA TEMPLATE HTML
    aluno.delete() # DELETANDO O ALUNO DO BANCO DE DADOS PELO PRIMARY KEY
    return redirect('alunos') # REDIRECT PARA A TELA DE ALUNOS
    
class AdminTemplateView(TemplateView):
    template_name = "administrador.html"

