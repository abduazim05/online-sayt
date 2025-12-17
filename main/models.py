from django.db import models

class Shop(models.Model):
    title = models.CharField( max_length=100 )
    description = models.TextField(null=True, blank=True)
    images = models.FileField( upload_to='images', max_length=100)
    price = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'

    def __str__(self):
        return self.title    