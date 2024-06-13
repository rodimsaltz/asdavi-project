from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from asdavi.models import Aluno
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from .models import Aluno


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

class EditarAlunoView(DetailView):  # FUNÇÃO PARA EXCLUIR ALUNO
    model = Aluno # PASSANDO OS PÂRAMETROS ESTABELECIDOS EM MODELS.PY
    template_name = "editar.html"
    def get_success_url(self):
        return redirect('alunos')
    
def Excluir_Aluno(request, pk): # FUNÇÃO PARA EXCLUIR ALUNO
    aluno = get_object_or_404(Aluno, pk=pk) # PEGANDO O PK DO ALUNO PELO FOR DA TEMPLATE HTML
    aluno.delete() # DELETANDO O ALUNO DO BANCO DE DADOS PELO PRIMARY KEY
    return redirect('alunos') # REDIRECT PARA A TELA DE ALUNOS


def login(request): # VIEW DA TELA DE LOGIN
    if request.method == "GET": # CASO O LOGIN JA TENHA SIDO FEITO
        return render(request, 'login.html')
    else: # CASO PRECISE FAZER O LOGIN 
        username = request.POST.get('username') # REQUISIÇÃO DO USER NO METODO GET
        senha = request.POST.get('senha') # REQUISIÇÃO DA SENHA NO METODO GET

        user = authenticate(username=username, password=senha) # FUNÇÃO DE AUTENTICAÇÃO

        if user: # CASO O LOGIN SEJA BEM SUCEDIDO
            auth_login(request, user)
            return redirect(reverse_lazy('administrador'))
        else: # CASO OS DADOS ESTEJAM ERRADOS
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})
        



@method_decorator(login_required, name='dispatch')
class AdminTemplateView(TemplateView):
    template_name = "administrador.html"


def generate_student_pdf(request, aluno_id):
    # Obtenha os dados do aluno
    aluno = Aluno.objects.get(id=aluno_id)

    # Renderize o template HTML com os dados do aluno
    html_string = render_to_string('info_alunos.html', {'aluno': aluno})

    # Crie uma resposta HTTP para PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="aluno_{aluno_id}.pdf"'

    # Gere o PDF
    pisa_status = pisa.CreatePDF(
        html_string, dest=response
    )
    # Verifique se houve algum erro na criação do PDF
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html_string + '</pre>')

    return response

