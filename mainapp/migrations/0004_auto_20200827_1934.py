# Generated by Django 2.0.1 on 2020-08-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_catetypeentity_fruitentity'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreEntity',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='店号')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='店名')),
                ('store_type', models.IntegerField(choices=[(0, '自营'), (1, '第三方')], db_column='type_', verbose_name='类型')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('city', models.CharField(db_index=True, max_length=50, verbose_name='城市')),
                ('creat_time', models.DateField(auto_now_add=True, verbose_name='成立时间')),
                ('last_time', models.DateField(auto_now=True, verbose_name='最后变更时间')),
            ],
            options={
                'verbose_name': '水果店',
                'verbose_name_plural': '水果店',
                'db_table': 't_store',
            },
        ),
        migrations.AlterModelOptions(
            name='catetypeentity',
            options={'ordering': ['-order_num'], 'verbose_name': '水果分类', 'verbose_name_plural': '水果分类'},
        ),
        migrations.AlterUniqueTogether(
            name='storeentity',
            unique_together={('name', 'city')},
        ),
    ]
