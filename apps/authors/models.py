from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"

    def __str__(self):
        return f"{self.name}"
