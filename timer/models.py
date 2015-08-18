from django.db import models
import json
from django.core.serializers.json import DjangoJSONEncoder

class Solve(models.Model):
    puzzle = models.CharField(max_length=10)
    scramble = models.CharField(max_length=50)
    duration = models.DecimalField(max_digits=7, decimal_places=3)
    time = models.DateTimeField(auto_now_add=True) # permanently set time of creation

    get_latest_by = "time"

    def to_JSON(self):
        return dict(
            date = self.time,
            duration = self.duration,
            scramble = self.scramble,
            puzzle = self.puzzle
        )
