# Generated by Django 4.2.2 on 2023-06-23 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muscico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('nacionalidade', models.CharField(choices=[('afegão', 'Afegão'), ('andorrano', 'Andorrano'), ('angolano', 'Angolano'), ('antiguano', 'Antiguano'), ('argelino', 'Argelino'), ('argentino', 'Argentino'), ('armênio', 'Armênio'), ('australiano', 'Australiano'), ('austríaco', 'Austríaco'), ('azeri', 'Azeri'), ('bahamense', 'Bahamense'), ('bangladês', 'Bangladês'), ('barbadiano', 'Barbadiano'), ('baremita', 'Baremita'), ('bielorrusso', 'Bielorrusso'), ('belga', 'Belga'), ('belizenho', 'Belizenho'), ('beninense', 'Beninense'), ('boliviano', 'Boliviano'), ('bósnio', 'Bósnio'), ('bechuano', 'Bechuano'), ('brasileiro', 'Brasileiro'), ('bruneano', 'Bruneano'), ('búlgaro', 'Búlgaro'), ('burquinense', 'Burquinense'), ('burundês', 'Burundês'), ('butanense', 'Butanense'), ('cabo-verdiano', 'Cabo-verdiano'), ('camaronense', 'Camaronense'), ('cambojano', 'Cambojano'), ('canadense', 'Canadense'), ('centroafricano', 'Centroafricano'), ('chadiano', 'Chadiano'), ('chinês', 'Chinês'), ('chileno', 'Chileno'), ('cookiano', 'Cookiano'), ('colombiano', 'Colombiano'), ('comoriano', 'Comoriano'), ('costa-riquenho', 'Costa-riquenho'), ('croata', 'Croata'), ('cubano', 'Cubano'), ('cipriota', 'Cipriota'), ('tcheco', 'Tcheco'), ('congolense', 'Congolense'), ('dinamarquês', 'Dinamarquês'), ('djibutiense', 'Djibutiense'), ('dominiquense', 'Dominiquense'), ('dominicano', 'Dominicano'), ('timorense', 'Timorense'), ('equatoriano', 'Equatoriano'), ('egípcio', 'Egípcio'), ('salvadorenho', 'Salvadorenho'), ('inglês', 'Inglês'), ('guinéu-equatoriano', 'Guinéu-equatoriano'), ('eritreu', 'Eritreu'), ('estoniano', 'Estoniano'), ('fijiano', 'Fijiano'), ('finlandês', 'Finlandês'), ('francês', 'Francês'), ('gabonense', 'Gabonense'), ('gambiano', 'Gambiano'), ('geórgico', 'Geórgico'), ('alemão', 'Alemão'), ('granadino', 'Granadino'), ('grego', 'Grego'), ('guatemalteco', 'Guatemalteco'), ('guineano', 'Guineano'), ('guineense', 'Guineense'), ('guianense', 'Guianense'), ('haitiano', 'Haitiano'), ('holandês', 'Holandês'), ('hondurenho', 'Hondurenho'), ('húngaro', 'Húngaro'), ('islandês', 'Islandês'), ('indiano', 'Indiano'), ('indonésio', 'Indonésio'), ('iraniano', 'Iraniano'), ('irlandês', 'Irlandês'), ('israelita', 'Israelita'), ('italiano', 'Italiano'), ('costa-marfinense', 'Costa-marfinense'), ('jamaicano', 'Jamaicano'), ('japonês', 'Japonês'), ('jordão', 'Jordão'), ('cazaque', 'Cazaque'), ('queniano', 'Queniano'), ('quiribatiano', 'Quiribatiano'), ('quirguistanês', 'Quirguistanês'), ('kuwaitiano', 'Kuwaitiano'), ('laosiano', 'Laosiano'), ('letoniano', 'Letoniano'), ('libanês', 'Libanês'), ('lesotiano', 'Lesotiano'), ('liberiano', 'Liberiano'), ('liechtensteinense', 'Liechtensteinense'), ('lituano', 'Lituano'), ('luxemburguês', 'Luxemburguês'), ('líbio', 'Líbio'), ('macedônio', 'Macedônio'), ('madagascarense', 'Madagascarense'), ('malaio', 'Malaio'), ('malauiano', 'Malauiano'), ('maldivo', 'Maldivo'), ('maliano', 'Maliano'), ('maltês', 'Maltês'), ('mauriciano', 'Mauriciano'), ('mauritano', 'Mauritano'), ('marshallino', 'Marshallino'), ('micronésio', 'Micronésio'), ('mexicano', 'Mexicano'), ('marroquino', 'Marroquino'), ('moldávio', 'Moldávio'), ('monegasco', 'Monegasco'), ('mongol', 'Mongol'), ('montenegrino', 'Montenegrino'), ('moçambicano', 'Moçambicano'), ('birmanês', 'Birmanês'), ('namibiano', 'Namibiano'), ('nauruano', 'Nauruano'), ('nepalês', 'Nepalês'), ('neozelandês', 'Neozelandês'), ('nicaraguense', 'Nicaraguense'), ('nigerino', 'Nigerino'), ('nigeriano', 'Nigeriano'), ('niuano', 'Niuano'), ('norte-coreano', 'Norte-coreano'), ('norueguês', 'Norueguês'), ('omanense', 'Omanense'), ('palestino', 'Palestino'), ('paquistanês', 'Paquistanês'), ('palauense', 'Palauense'), ('panamenho', 'Panamenho'), ('papuásio', 'Papuásio'), ('paraguaio', 'Paraguaio'), ('peruano', 'Peruano'), ('filipino', 'Filipino'), ('polonês', 'Polonês'), ('português', 'Português'), ('catarense', 'Catarense'), ('romeno', 'Romeno'), ('russoruandês', 'Russoruandês'), ('samoano', 'Samoano'), ('santa-lucense', 'Santa-lucense'), ('são-cristovense', 'São-cristovense'), ('são-marinense', 'São-marinense'), ('são-tomense', 'São-tomense'), ('são-vicentino', 'São-vicentino'), ('escocês', 'Escocês'), ('senegalense', 'Senegalense'), ('servio', 'Servio'), ('seichelense', 'Seichelense'), ('serra-leonês', 'Serra-leonês'), ('singapurense', 'Singapurense'), ('eslovaco', 'Eslovaco'), ('salomônico', 'Salomônico'), ('somali', 'Somali'), ('sul-africano', 'Sul-africano'), ('coreano', 'Coreano'), ('sul-sudanense', 'Sul-sudanense'), ('espanhol', 'Espanhol'), ('srilankês', 'Srilankês'), ('sudanense', 'Sudanense'), ('surinamês', 'Surinamês'), ('suazi', 'Suazi'), ('sueco', 'Sueco'), ('suíço', 'Suíço'), ('sírio', 'Sírio'), ('tadiquistão', 'Tadiquistão'), ('tajique', 'Tajique'), ('tanzaniano', 'Tanzaniano'), ('tailandês', 'Tailandês'), ('togolês', 'Togolês'), ('tonganês', 'Tonganês'), ('trinitário', 'Trinitário'), ('tunisiano', 'Tunisiano'), ('turcomeno', 'Turcomeno'), ('turco', 'Turco'), ('tuvaluano', 'Tuvaluano'), ('ucraniano', 'Ucraniano'), ('ugandês', 'Ugandês'), ('uruguaio', 'Uruguaio'), ('árabe', 'Árabe'), ('britânico', 'Britânico'), ('americano', 'Americano'), ('uzbeque', 'Uzbeque'), ('vanuatuano', 'Vanuatuano'), ('venezuelano', 'Venezuelano'), ('vietnamita', 'Vietnamita'), ('galês', 'Galês'), ('iemenita', 'Iemenita'), ('zambiano', 'Zambiano'), ('zimbabueano', 'Zimbabueano')], max_length=20)),
                ('dt_nascimento', models.DateField()),
            ],
            options={
                'verbose_name': 'Musico',
                'verbose_name_plural': 'Musicos',
            },
        ),
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('n_serie', models.IntegerField()),
                ('musico', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.muscico')),
            ],
            options={
                'verbose_name': 'Instrumento',
                'verbose_name_plural': 'Instrumentos',
            },
        ),
    ]