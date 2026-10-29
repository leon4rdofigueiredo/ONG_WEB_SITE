from datetime import date

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import VoluntarioForm
from .models import PERIODO_CHOICES, Projeto

# os dados da equipe e dos projetos ficam em listas aqui e o html monta os cartoes com {% for %}.
# assim, pra mudar um texto ou acrescentar um projeto, so mexe nessas listas e nao no html.

def inicio(request):
    return render(request, 'inicio.html')

def sobre(request):
    equipe = [
        {'nome': 'Marcos', 'funcao': 'Responsável pelo Futebol', 'foto': 'equipe_marcos.jpg'},
        {'nome': 'Claudinei', 'funcao': 'Responsável pelas Artes Marciais', 'foto': 'equipe_claudinei.jpg'},
        {'nome': 'Rouglan', 'funcao': 'Responsável pelo curso de Elétrica', 'foto': 'equipe_rouglan.jpg'},
        {'nome': 'João Pedro', 'funcao': 'Responsável pelo curso de Informática', 'foto': 'equipe_joao_pedro.jpg'},
        {'nome': 'Arina', 'funcao': 'Responsável pelo Ballet na Igreja', 'foto': 'equipe_arina.jpg'},
        {'nome': 'Rodrigão', 'funcao': 'Responsável pelo Sopão Solidário', 'foto': 'equipe_rodrigao.jpg'},
        {'nome': 'Rômulo Fortunato', 'funcao': 'Responsável pelo Muay Thai', 'foto': 'equipe_romulo.jpg'},
        {'nome': 'Wesley', 'funcao': 'Responsável pelo Taekwondo', 'foto': 'equipe_wesley.jpg'},
        {'nome': 'Pamela', 'funcao': 'Responsável pela alfabetização e reforço escolar', 'foto': 'equipe_pamela.jpg'},
    ]
    return render(request, 'sobre.html', {'equipe': equipe})

def projetos(request):
    lista = [
        {
            'nome': 'Futebol',
            'titulo': 'Saúde, Lazer e Valores',
            'foto': 'projeto_futebol.jpg',
            'responsavel': 'Marcos Gomes e Claudinei',
            'situacao': 'Em andamento',
            'historico': 'O futebol sempre foi uma ponte de transformação no bairro. Já gerou dezenas de histórias como a do Claudinei — vidas que encontraram disciplina, foco e novos caminhos. Hoje queremos retomar esse impacto — e isso depende de você.',
            'infraestrutura': ['Local para realização das partidas (Campo São Jorge)', 'Sistema de som', 'Espaço para o público (pais, responsáveis, etc.)', 'Limpeza do campo'],
            'materiais': ['Bola de futebol', 'Uniformes e tênis adequados para os participantes', 'Apitos e material de arbitragem', 'Cones e marcadores para campo'],
            'objetivos': ['Oferecer 52 treinos ao ano.', 'Garantir café da manhã para 80 crianças todos os sábados.', 'Criar um canal entre esporte e oportunidades educacionais (informática/elétrica).', 'Ampliar o acesso de crianças vulneráveis a um ambiente seguro e acolhedor.'],
            'destaque': 'Com R$50 você garante o lanche de todas as crianças por um sábado.',
        },
        {
            'nome': 'Sopão Solidário',
            'titulo': 'Alimentação que Cuida',
            'foto': 'projeto_sopao.jpg',
            'responsavel': 'José Carlos Rodrigues',
            'situacao': 'Em andamento',
            'historico': 'Começamos esse projeto no início de 2024. A princípio ele aconteceria com intervalo de duas semanas, por conta dos custos, mas no dia da inauguração percebemos a necessidade da comunidade. Na semana seguinte continuamos sem intervalos até hoje.',
            'infraestrutura': ['Cozinha equipada', 'Mesas para servir a sopa', 'Espaço para acomodar as famílias', 'Iluminação', 'Climatização'],
            'materiais': ['Ingredientes para o preparo do sopão (legumes, carne, arroz, etc.)', 'Panelas industriais', 'Talheres e pratos descartáveis', 'Embalagens para entrega de sopa'],
            'objetivos': ['Distribuir 100 porções de sopa semanalmente, totalizando 5.200 refeições durante o ano.', 'Variar os cardápios semanalmente.', 'Fazer uma grande ceia de Natal.'],
            'destaque': 'Gastamos em média R$85 a R$100 por semana, dependendo do cardápio.',
        },
        {
            'nome': 'Curso de Informática',
            'titulo': 'Formação Profissional',
            'foto': 'projeto_informatica.jpg',
            'responsavel': 'João Pedro',
            'situacao': 'Precisa colocar telhado no terraço',
            'historico': 'Três profissionais de TI da igreja decidiram mudar o futuro de jovens sem oportunidade. Conseguimos algumas máquinas — mas o espaço precisa de reforma urgente.',
            'infraestrutura': ['Preparação do laboratório de informática', 'Instalação de rede de internet', 'Climatização do laboratório', 'Resolver problema de infiltração no terraço'],
            'materiais': ['12 computadores', 'Bancadas, mesas e cadeiras de escritório', 'Software educacional e aplicativos para aulas', 'Projetor ou tela touch'],
            'objetivos': ['Formar 36 alunos por ciclo.', 'Ensinar montagem, manutenção e conceitos de programação.', 'Criar uma trilha para inserção no mercado de trabalho.'],
            'destaque': 'Sua doação equipa o laboratório e prepara jovens para o mercado.',
        },
        {
            'nome': 'Artes Marciais',
            'titulo': 'Disciplina e Autoconfiança',
            'foto': 'projeto_artes_marciais.jpg',
            'responsavel': 'Claudinei, Wesley e Rômulo',
            'situacao': 'Em andamento',
            'historico': 'Com professores voluntários e muitos sonhos, estamos prontos para iniciar um espaço onde disciplina, autocontrole e respeito moldam jovens todos os dias.',
            'infraestrutura': ['Ampliação da área da cantina para as atividades de lutas', 'Climatização'],
            'materiais': ['Tatames e colchonetes', 'Uniformes (kimonos para jiu-jitsu, uniformes para taekwondo e muay thai)', 'Equipamentos de proteção (capacetes, luvas, protetores bucais)'],
            'objetivos': ['Criar turmas de Jiu-jitsu, Taekwondo e Muay Thai.', 'Oferecer duas aulas por semana.', 'Formar instrutores locais.'],
            'destaque': '',
        },
        {
            'nome': 'Curso de Elétrica',
            'titulo': 'Formação Profissional',
            'foto': 'projeto_eletrica.jpg',
            'responsavel': 'Rouglan',
            'situacao': 'Em breve',
            'historico': 'Este curso nasceu quando um adolescente chorou dizendo que "não seria nada na vida". Decidimos provar o contrário.',
            'infraestrutura': ['Sala para aulas práticas com bancadas de trabalho', 'Equipamento de segurança (extintores, sinalização de segurança)'],
            'materiais': ['Ferramentas de elétrica (multímetros, chaves de fenda, alicates, etc.)', 'Materiais didáticos (livros, apostilas)', 'Equipamentos de segurança (luvas, óculos, botas)'],
            'objetivos': ['Ensinar nossos jovens uma profissão que possibilite a inserção no mercado de trabalho.'],
            'destaque': '',
        },
        {
            'nome': 'Ballet na Igreja',
            'titulo': 'Arte que Transforma',
            'foto': 'projeto_ballet.jpg',
            'responsavel': 'Arina Paiva',
            'situacao': 'Em andamento',
            'historico': 'O ballet já mudou a autoestima de muitas meninas da igreja e do bairro. Queremos ampliar — muito.',
            'infraestrutura': ['Sala para aulas práticas com barras e espelhos de corpo inteiro', 'Armários, som e iluminação', 'Piso liso', 'Climatização'],
            'materiais': ['Maiôs, collants, saias e meias-calças', 'Roupa para as aulas, como leotards, leggings e tops', 'Sapatilhas de ballet'],
            'objetivos': ['Chegar a 50 alunas.', 'Criar turmas por nível.', 'Realizar espetáculos anuais no bairro.'],
            'destaque': 'Com R$100 você veste uma bailarina pela primeira vez.',
        },
    ]
    return render(request, 'projetos.html', {'projetos': lista})

def doacao(request):
    return render(request, 'doacao.html')

# os projetos que o voluntario pode escolher agora ficam no banco (model Projeto).
# o formulario e o filtro do painel usam a mesma tabela, entao pra um projeto entrar ou sair
# e so mexer pelo admin do Django (/admin-django/)

# situacao de cada cadastro no painel:
# Pendente = ninguem analisou ainda | Ativo = aceito e ajudando
# Inativo = era ativo e parou | Recusado = analisado e nao aceito
STATUS_VOLUNTARIO = ['Pendente', 'Ativo', 'Inativo', 'Recusado']

def voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro enviado! Obrigado por querer ajudar, em breve entraremos em contato.')
            # redireciona pra que um F5 nao envie o mesmo cadastro de novo
            return redirect('voluntario')
    else:
        form = VoluntarioForm()

    # o html marca de novo o que a pessoa ja tinha escolhido quando o envio volta com erro
    if form.is_bound:
        periodo_escolhido = form.data.get('periodo', '')
        projetos_escolhidos = form.data.getlist('projetos')
    else:
        periodo_escolhido = 'Manhã'
        projetos_escolhidos = []

    return render(request, 'voluntario.html', {
        'form': form,
        'projetos': Projeto.objects.all(),
        'periodos': [valor for valor, _ in PERIODO_CHOICES],
        'periodo_escolhido': periodo_escolhido,
        'projetos_escolhidos': projetos_escolhidos,
    })

def login_admin(request):
    # login TEMPORARIO pra testar a tela enquanto nao tem banco: usuario admin, senha admin.
    # so funciona com DEBUG = True (no computador de quem esta desenvolvendo), entao nao vale no site publicado.
    # quem fizer o backend troca essa funcao pelo LoginView do Django; o html ja usa os nomes que ele espera
    # (username, password, form.errors e next)
    erro = False
    if request.method == 'POST':
        usuario = request.POST.get('username', '')
        senha = request.POST.get('password', '')
        if settings.DEBUG and usuario == 'admin' and senha == 'admin':
            return redirect('painel_admin')
        erro = True
    return render(request, 'login.html', {'erro': erro})

def painel_admin(request):
    # dados de exemplo so pra montar a tela, ainda nao tem banco.
    # a data e um date (nao texto) pra dar pra ordenar por mais recente, igual vai ser com o banco
    # o backend troca essa lista pelos cadastros reais, com os mesmos nomes de campo do formulario de voluntario
    cadastros = [
        {'nome': 'Voluntário Exemplo 1', 'telefone': '(21) 90000-0001', 'email': 'exemplo1@email.com',
         'periodo': 'Manhã', 'projetos': ['Futebol', 'Sopão Solidário'], 'horas': 4, 'data': date(2026, 10, 20), 'status': 'Ativo'},
        {'nome': 'Voluntário Exemplo 2', 'telefone': '(21) 90000-0002', 'email': 'exemplo2@email.com',
         'periodo': 'Noite', 'projetos': ['Curso de Informática'], 'horas': 6, 'data': date(2026, 10, 21), 'status': 'Pendente'},
        {'nome': 'Voluntário Exemplo 3', 'telefone': '(21) 90000-0003', 'email': 'exemplo3@email.com',
         'periodo': 'Tarde', 'projetos': ['Ballet na Igreja', 'Alfabetização e Reforço Escolar'], 'horas': 3, 'data': date(2026, 10, 22), 'status': 'Recusado'},
        {'nome': 'Voluntário Exemplo 4', 'telefone': '(21) 90000-0004', 'email': 'exemplo4@email.com',
         'periodo': 'Manhã', 'projetos': ['Artes Marciais (Jiu-jitsu, Taekwondo e Muay Thai)'], 'horas': 8, 'data': date(2026, 10, 24), 'status': 'Inativo'},
        {'nome': 'Voluntário Exemplo 5', 'telefone': '(21) 90000-0005', 'email': 'exemplo5@email.com',
         'periodo': 'Tarde', 'projetos': ['Curso de Elétrica', 'Futebol'], 'horas': 2, 'data': date(2026, 10, 25), 'status': 'Pendente'},
    ]

    # o resumo conta os periodos so de quem esta Ativo (quem esta de fato ajudando)
    ativos_por_periodo = {'Manhã': 0, 'Tarde': 0, 'Noite': 0}
    por_status = {'Pendente': 0, 'Ativo': 0, 'Inativo': 0, 'Recusado': 0}
    for c in cadastros:
        por_status[c['status']] = por_status[c['status']] + 1
        if c['status'] == 'Ativo':
            ativos_por_periodo[c['periodo']] = ativos_por_periodo[c['periodo']] + 1

    return render(request, 'painel.html', {
        'cadastros': cadastros,
        'ativos_por_periodo': ativos_por_periodo,
        'por_status': por_status,
        'lista_status': STATUS_VOLUNTARIO,
        'projetos': Projeto.objects.all(),
    })
