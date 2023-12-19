from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    author_id = models.ForeignKey("authors.Authors", on_delete=models.CASCADE)
    category_id = models.ForeignKey("categories.Categories", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return f"{self.title}"
