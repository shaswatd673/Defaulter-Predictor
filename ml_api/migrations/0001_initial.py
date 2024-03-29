# Generated by Django 2.2.3 on 2019-10-10 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Principal', models.IntegerField()),
                ('terms', models.IntegerField()),
                ('age', models.IntegerField()),
                ('Gender', models.IntegerField(choices=[(0, 'male'), (1, 'female')])),
                ('weekend', models.IntegerField(choices=[(0, 'weekday'), (1, 'weekend')])),
                ('EDUCATION', models.CharField(choices=[('High School or Below', 'High School or Below'), ('college', 'college'), ('Bechalor', 'Bechalor'), ('Master or Above', 'Master or Above')], max_length=100)),
            ],
        ),
    ]
