from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
import uuid


# Create your models here.

class Genre(models.Model):
    name = models.CharField('장르', max_length=200, help_text='새로운 장르를 입력하세요')

    class Meta:
        verbose_name = '장르'
        verbose_name_plural = '장르'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField('언어', max_length=50)

    class Meta:
        verbose_name = '언어'
        verbose_name_plural = '언어'
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField("제목", max_length=200)
    author = models.ForeignKey('Author', verbose_name='저자', on_delete=models.SET_NULL, null=True)

    summary = models.TextField('내용', max_length=1000, help_text='간략한 줄거리를 입력하세요')
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13자리 <a href="https://www.isbn-international.org/content/what-isbn">ISBN</a>')

    genre = models.ManyToManyField(Genre, verbose_name='장르', help_text='장르를 선택하세요')
    language = models.ManyToManyField(Language, verbose_name='언어', help_text='언어를 선택하세요')

    class Meta:
        verbose_name = '책'
        verbose_name_plural = '책'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = "장르"


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='책인스턴스의 고유번호')
    book = models.ForeignKey('Book', verbose_name='책', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField('출판사', max_length=200)
    due_back = models.DateField('만료', null=True, blank=True)
    borrower = models.ForeignKey(User, verbose_name='대여자', on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', '점검중'),
        ('o', '대여중'),
        ('a', '대여가능'),
        ('r', '예약'),
    )

    status = models.CharField(
        verbose_name='상태',
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='대여 가능 여부',
    )

    class Meta:
        verbose_name = '책인스턴스'
        verbose_name_plural = '책인스턴스'
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        return f'{self.id} ({self.book.title})'

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False


class Author(models.Model):
    id = models.IntegerField('작가번호', primary_key=True, null=False, help_text='작가 고유번호')
    first_name = models.CharField('이름', max_length=100)
    last_name = models.CharField('성', max_length=100)
    date_of_birth = models.DateField('탄생일', null=True, blank=True)
    date_of_death = models.DateField('사망일', null=True, blank=True)

    class Meta:
        verbose_name = '저자'
        verbose_name_plural = '저자'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
