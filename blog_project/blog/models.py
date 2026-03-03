from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="tytuł")
    content = models.TextField(verbose_name="treść")
    published_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name="opublikowany")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    def __str__(self):
        return self.title

    def word_count(self):
        return len(self.content.split())

    def reading_time(self):
        """Czas czytania w minutach (200 słów/min)."""
        return max(1, self.word_count() // 200)

    def get_excerpt(self, length=100):
        """Zwraca skrócony fragment treści."""
        if len(self.content) <= length:
            return self.content
        return self.content[:length] + '...'

    @property
    def is_long(self):
        """Czy post jest długi (>1000 słów)."""
        return self.word_count() > 1000