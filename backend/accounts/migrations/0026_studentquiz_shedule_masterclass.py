# Generated by Django 4.2.6 on 2024-01-10 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_rename_enrolled_at_studentassignment_submitted_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_at', models.DateTimeField(auto_now=True)),
                ('mark', models.IntegerField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.studentprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Shedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateField()),
                ('about', models.TextField(max_length=1000)),
                ('completed', models.BooleanField(default=False)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.teacherprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Masterclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateField()),
                ('time', models.TimeField()),
                ('about', models.TextField(max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.coursecategory')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.teacherprofile')),
            ],
        ),
    ]