from django.db import models

class MoonMemory(models.Model):
    date = models.DateField(unique=True)
    phase = models.CharField(max_length=50)
    sign = models.CharField(max_length=50)
    emoji = models.CharField(max_length=10)
    description = models.TextField()
    emotion_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Memory of {self.date} - {self.sign} {self.phase}"
