# Generated by Django 4.0.2 on 2022-03-27 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('body', models.TextField()),
            ],
            options={
                'verbose_name': 'Artigo',
                'verbose_name_plural': 'Artigos',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='Sobrenome')),
            ],
            options={
                'verbose_name': 'Autores',
                'verbose_name_plural': 'Autor',
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Categoria')),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categorias',
                'verbose_name_plural': 'categoria',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.article')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.author')),
                ('category', models.ManyToManyField(related_name='publishes', to='core.Category')),
            ],
            options={
                'verbose_name': 'Publicação',
                'verbose_name_plural': 'Publicações',
                'db_table': 'publish',
            },
        ),
    ]
