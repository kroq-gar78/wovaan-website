from django.db import models

class Solve(models.Model):
    puzzle = models.CharField(max_length=10)
    scramble = models.CharField(max_length=50)
    duration = models.DecimalField(max_digits=7, decimal_places=3)
    time = models.DateTimeField(auto_now_add=True) # permanently set time of creation

    get_latest_by = "time"
