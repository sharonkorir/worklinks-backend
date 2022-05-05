# Generated by Django 3.2.7 on 2022-05-03 12:32

import cloudinary.models
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_employer', models.BooleanField(default=False)),
                ('is_jobseeker', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userId', models.IntegerField()),
                ('content', models.CharField(max_length=255)),
                ('post', models.CharField(max_length=255)),
                ('like', models.IntegerField()),
                ('dislike', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=255)),
                ('requirements', models.TextField()),
                ('jobtype', models.TextField(choices=[('Part Time', 'Part-Time'), ('Remote', 'Remote'), ('Full Time', 'Full-Time')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MpesaPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('type', models.TextField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('contact', models.TextField()),
            ],
            options={
                'verbose_name': 'Mpesa Payment',
                'verbose_name_plural': 'Mpesa Payments',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name=django.contrib.auth.models.User)),
                ('full_name', models.CharField(max_length=255)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('email', models.CharField(max_length=255)),
                ('bio', models.CharField(max_length=255)),
                ('work_experience', models.CharField(blank=True, max_length=255)),
                ('profile_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('address', models.CharField(max_length=100)),
                ('resume', models.FileField(blank=True, upload_to='')),
                ('skills', models.CharField(blank=True, max_length=255)),
                ('referees', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('email', models.CharField(max_length=255)),
                ('contact', models.IntegerField()),
                ('location', models.IntegerField(blank=True)),
                ('address', models.CharField(max_length=255)),
                ('company_bio', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('company_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Jobseeker',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.employer')),
                ('profile_photo', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('bio', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('contact', models.CharField(blank=True, max_length=30)),
                ('availability', models.CharField(blank=True, max_length=20)),
                ('salary', models.IntegerField()),
                ('name', models.IntegerField()),
                ('phone_no', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
