
from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    resume_file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    analysis_result = models.TextField(blank=True)
    ats_score = models.IntegerField(default=0)

    def __str__(self):
        return self.name