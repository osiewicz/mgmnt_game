from django.db import models

class HtmlContent(models.Model):
    keyword = models.CharField(max_length=31)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.keyword
