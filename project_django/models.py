from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ім'я")
    last_name = models.CharField(max_length=100, verbose_name="Прізвище")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Контактний телефон")
    notes = models.TextField(blank=True, null=True, verbose_name="Примітки")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contacts'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.phone}"