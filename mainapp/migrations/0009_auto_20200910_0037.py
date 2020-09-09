# Generated by Django 2.0.1 on 2020-09-09 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_realprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartEntity',
            fields=[
                ('no', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='购物车编号')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.UserEntity', verbose_name='账号')),
            ],
            options={
                'verbose_name': '购物车表',
                'verbose_name_plural': '购物车表',
                'db_table': 't_cart',
            },
        ),
        migrations.AlterField(
            model_name='realprofile',
            name='image2',
            field=models.ImageField(upload_to='user/real', verbose_name='反面照'),
        ),
        migrations.AlterField(
            model_name='storeentity',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='store/logo', verbose_name='LOGO'),
        ),
    ]
