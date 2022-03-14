# Generated by Django 2.2.9 on 2022-02-18 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentticket',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Question'),
        ),
        migrations.AddField(
            model_name='tutorticket',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('Maths', 'Maths'), ('Programming', 'Programming'), ('others', 'others'), ('Science', 'Science')], default='others', max_length=30),
        ),
    ]
