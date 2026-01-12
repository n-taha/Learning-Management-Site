from django.db import models
from django.contrib.auth.models import User

class AdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='additional_info')
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    school = models.CharField(max_length=150, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True,default='profile_pics/default.png')
    district = models.CharField(max_length=100, blank=True, null=True)
    upazilla = models.CharField(max_length=100, blank=True, null=True)

    # Batch year options
    BATCH_YEAR_CHOICES = [(year, year) for year in range(2026, 2035)]
    batch_year = models.IntegerField(choices=BATCH_YEAR_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Additional Info"
