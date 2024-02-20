# Generated by Django 4.2.7 on 2023-12-16 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_subcategory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='product.product'),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('data_type', models.CharField(choices=[], max_length=255)),
                ('regex', models.CharField(max_length=255)),
                ('validations', models.JSONField()),
                ('choices', models.CharField(max_length=500)),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.subcategory')),
            ],
        ),
    ]