from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

# periodos que aparecem no formulario de voluntario e no filtro do painel
PERIODO_CHOICES = [
    ('Manhã', 'Manhã'),
    ('Tarde', 'Tarde'),
    ('Noite', 'Noite'),
]

# aceita fixo (XX) XXXX-XXXX e celular (XX) XXXXX-XXXX.
# o mesmo formato esta no pattern do campo em voluntario.html
validar_telefone = RegexValidator(
    r'^\(\d{2}\) \d{4,5}-\d{4}$',
    'Informe o telefone no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX.')


class Projeto(models.Model):
    # os projetos iniciais sao criados pela migracao 0002_popular_projetos.
    # pra acrescentar um projeto novo, cadastra pelo admin do Django (/admin-django/)
    nome = models.CharField('nome', max_length=100, unique=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'projeto'
        verbose_name_plural = 'projetos'

    def __str__(self):
        return self.nome


class Voluntario(models.Model):
    nome = models.CharField('nome', max_length=150)
    telefone = models.CharField('telefone', max_length=20, validators=[validar_telefone])
    email = models.EmailField('e-mail')
    periodo = models.CharField('disponibilidade', max_length=10, choices=PERIODO_CHOICES)
    projetos = models.ManyToManyField(Projeto, verbose_name='projetos de interesse')
    # 0 a 20, os mesmos limites da caixa e da barra na tela
    horas = models.PositiveSmallIntegerField(
        'horas por semana', validators=[MinValueValidator(0), MaxValueValidator(20)])

    class Meta:
        verbose_name = 'voluntário'
        verbose_name_plural = 'voluntários'

    def __str__(self):
        return self.nome
