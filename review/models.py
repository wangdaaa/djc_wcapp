from django.db import models

# Create your models here.


class ReviewGameFileDB(models.Model):
    """

    """
    name = models.CharField(max_length=128,null=False)
    image = models.CharField(max_length=128,null=True)
    description = models.CharField(max_length=512,null=True)
    available = models.BooleanField(default=True)
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'review_game_file'

