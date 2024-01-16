# Generated by Django 5.0.1 on 2024-01-16 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog', '0010_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.useradmin'),
        ),
        migrations.AlterField(
            model_name='useradmin',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_admin_groups', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='useradmin',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_admin_permissions', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
