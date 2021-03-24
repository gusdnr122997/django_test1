# Generated by Django 3.1.7 on 2021-03-08 01:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='이름')),
                ('last_name', models.CharField(max_length=100, verbose_name='성')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='사망일')),
            ],
            options={
                'verbose_name': '저자',
                'verbose_name_plural': '저자',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('summary', models.TextField(help_text='간략한 줄거리를 입력하세요', max_length=1000, verbose_name='내용')),
                ('isbn', models.CharField(help_text='13자리 <a href="https://www.isbn-international.org/content/what-isbn">ISBN</a>', max_length=13, verbose_name='ISBN')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.author', verbose_name='저자')),
            ],
            options={
                'verbose_name': '책',
                'verbose_name_plural': '책',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='새로운 장르를 입력하세요', max_length=200, verbose_name='장르')),
            ],
            options={
                'verbose_name': '장르',
                'verbose_name_plural': '장르',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='언어')),
            ],
            options={
                'verbose_name': '언어',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='책인스턴스의 고유번호', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200, verbose_name='출판사')),
                ('due_back', models.DateField(blank=True, null=True, verbose_name='만료')),
                ('status', models.CharField(blank=True, choices=[('m', '점검중'), ('o', '대여중'), ('a', '대여가능'), ('r', '예약')], default='m', help_text='대여 가능 여부', max_length=1, verbose_name='상태')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.book', verbose_name='책')),
            ],
            options={
                'verbose_name': '책인스턴스',
                'verbose_name_plural': '책인스턴스',
                'ordering': ['due_back'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='장르를 선택하세요', to='catalog.Genre', verbose_name='장르'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(help_text='언어를 선택하세요', to='catalog.Language', verbose_name='언어'),
        ),
    ]