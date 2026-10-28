from django.db import migrations

# projetos que ja apareciam no formulario de voluntario antes de existir o banco
PROJETOS_INICIAIS = ['Futebol', 'Sopão Solidário', 'Curso de Informática', 'Curso de Elétrica',
                     'Artes Marciais (Jiu-jitsu, Taekwondo e Muay Thai)', 'Ballet na Igreja',
                     'Alfabetização e Reforço Escolar']


def criar_projetos(apps, schema_editor):
    Projeto = apps.get_model('site_ong', 'Projeto')
    for nome in PROJETOS_INICIAIS:
        Projeto.objects.get_or_create(nome=nome)


def apagar_projetos(apps, schema_editor):
    Projeto = apps.get_model('site_ong', 'Projeto')
    Projeto.objects.filter(nome__in=PROJETOS_INICIAIS).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('site_ong', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(criar_projetos, apagar_projetos),
    ]
