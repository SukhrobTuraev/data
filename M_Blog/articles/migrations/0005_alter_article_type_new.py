# Generated by Django 4.1.3 on 2022-11-13 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_type_new_alter_article_id_alter_comment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type_new',
            field=models.CharField(choices=[('Sport', 'Sport'), ('Jahon', 'Jahon')], max_length=10),
        ),
    ]
