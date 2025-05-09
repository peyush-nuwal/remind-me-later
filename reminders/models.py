from django.db import models

class Reminder(models.Model):
    message = models.CharField(max_length=255)
    remind_at = models.DateTimeField()
    reminder_type = models.CharField(max_length=100)

    def __str__(self):
        return f"Reminder: {self.message} at {self.remind_at}"
