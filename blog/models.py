from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')# зв'язок із іншою моделлю.
    title = models.CharField(max_length=200)#для текстових полів з обмеженням кількісті символів.
    text = models.TextField()#великі блоки тексту без обмежень. 
    created_date = models.DateTimeField(default=timezone.now)#дата та час
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title