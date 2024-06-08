"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from asdavi.views import IndexTemplateView, PagamentoTemplateView, DoacaoTemplateView, LoginTemplateView, CadastroCreateView, PesquisaAlunoView, EditarAlunoView,AdminTemplateView
from asdavi import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexTemplateView.as_view(), name="index" ),
    path('pagamento/', PagamentoTemplateView.as_view(), name="pagamento" ),
    path('doacao/', DoacaoTemplateView.as_view(), name ="doacao"),
    path('login/', LoginTemplateView.as_view(), name="login"),
    path('cadastro/', CadastroCreateView.as_view(), name="cadastro"),
    path('listaralunos/', PesquisaAlunoView.as_view(), name="alunos"),
    path('editar/<int:pk>', EditarAlunoView.as_view(), name = "editar"),
    path('excluir/<int:pk>', views.Excluir_Aluno, name = "excluir"),
    path('administrador/', AdminTemplateView.as_view(), name="admin"),
]
