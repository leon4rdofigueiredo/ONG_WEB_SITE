# Caminho da Esperança – Instituto Social

Site do projeto social **Caminho da Esperança**, da Primeira Igreja Batista em Retiro São Joaquim.
Feito com **Django** (Python), **HTML** e **CSS**.

## Páginas

- **Início** – apresentação, como ajudar e resumo dos projetos
- **Sobre** – história, pesquisa no bairro, equipe e testemunho
- **Projetos** – detalhes de cada projeto (futebol, sopão, informática, artes marciais, elétrica e ballet)
- **Doação** – PIX e contato pelo WhatsApp
- **Seja Voluntário** – formulário de inscrição (por enquanto só visual)
- **Área do administrador** (`/admin/`) – tela de login, sem link no menu
- **Painel do administrador** (`/admin/painel/`) – tabela com os cadastros de voluntários, busca e filtros por projeto e período



## Estrutura

```
caminho/            configurações do Django (settings.py, urls.py)
site_ong/
  views.py          funções de cada página e textos dos projetos/equipe
  models.py         tabelas do banco (Voluntario e Projeto)
  forms.py          formulário de voluntário (validação)
  admin.py          cadastros no admin do Django (/admin-django/)
  migrations/       criação das tabelas e dos projetos iniciais
  templates/        páginas HTML (base.html tem o menu e o rodapé; chamada.html é a faixa do final de Sobre e Projetos)
  static/css/       estilo do site
  static/imagens/   imagens
manage.py
build.sh            comandos que o Render roda a cada deploy
.env.example        modelo das variáveis do banco (copiar para .env)
```
