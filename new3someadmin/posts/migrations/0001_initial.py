# Generated by Django 3.0.5 on 2020-05-02 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Catagory',
                'verbose_name_plural': 'Catagorys',
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('img', models.ImageField(upload_to='postimg/')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('categorie', models.ManyToManyField(related_name='categaties', to='posts.Categories')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
