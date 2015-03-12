from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

    def src_url(self):
        return self.url.replace("watch?v=", "v/")

    def __unicode__(self):
        return self.name