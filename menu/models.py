from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    ordering = models.PositiveIntegerField()

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.name
