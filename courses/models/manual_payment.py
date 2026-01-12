from django.db import models
from django.contrib.auth.models import User
from courses.models.course import Course

class ManualPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payer_number = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.user.username} - {self.course.name} - {self.payment_method}"
