from django.db import models

class SlotMachine(models.Model):
    name = models.CharField(max_length=100, default="Classic Slot Machine")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
