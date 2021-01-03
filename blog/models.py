from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # models은 Post가 장고 모델임을 의미합니다. 이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 됩니다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #  models.ForeignKey는 다른 모델에 대한 링크를 의미합니다
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title