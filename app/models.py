from django.db import models

# Create your models here.


class GameFileDB(models.Model):
    """

    """
    name = models.CharField(max_length=128,null=False)
    image = models.CharField(max_length=128,null=False)
    description = models.CharField(max_length=512,null=True)
    available = models.BooleanField(default=False)
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'game_file_db'

