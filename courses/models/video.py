from django.db import models
from courses.models import Course

class Video(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    serial_number = models.IntegerField()
    video_id = models.CharField(max_length=100)
    is_preview = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        vid = self.video_id.strip()

        if "watch?v=" in vid:
            vid = vid.split("watch?v=")[-1]
        elif "youtu.be/" in vid:
            vid = vid.split("youtu.be/")[-1]
        elif "shorts/" in vid:
            vid = vid.split("shorts/")[-1]
        elif "embed/" in vid:
            vid = vid.split("embed/")[-1]

        # remove extra params
        vid = vid.split("&")[0]

        self.video_id = vid
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
