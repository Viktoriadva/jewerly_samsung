import datetime
from django.db import models
from django.utils import timezone

class HowLooks(models.Model):
    title_of_img = models.CharField('Название изображения', max_length = 40)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title_of_img
class Article(models.Model):
    article_title = models.CharField('Объявление', max_length = 50)

    article_text = models.TextField('описание продукта')
    pub_date = models.DateTimeField('дата публикации')
    def __str__(self):
        return self.article_title
    def was_published_recently(self):
        return self.pub_date>= ((timezone.now) - datetime.timedelta(days = 5))
    class Meta:
        verbose_name = 'Украшение'
        verbose_name_plural='Украшения'
    




class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    #то что все коомент будут прикреплены к этой модели and для того чтобы удалять внутри
    author_name = models.CharField('Name of the author', max_length = 50)
    comment_text = models.CharField('текст of comment', max_length = 50)

    #все это информация для лданги что мы будем сохранять в базе данных и связб тоже указали
    def __str__(self):
        return self.author_name
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural='Комментарии'