from django.db import models
import json
from django.core.serializers.json import DjangoJSONEncoder

from wovaan.scrambler import scramble_cube

class Solve(models.Model):
    puzzle = models.ForeignKey('Puzzle')
    scramble = models.CharField(max_length=50)
    duration = models.DecimalField(max_digits=7, decimal_places=3)
    date = models.DateTimeField(auto_now_add=True) # permanently set date/time of creation

    get_latest_by = "date"

    def __str__(self):
        return '%s %.2fs' % (str(self.puzzle), self.duration)

class Puzzle(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    size = models.PositiveIntegerField(default=3)
    scrambler = models.CharField(max_length=20)

    def getScrambler(self):
        if(self.scrambler == "randomstate" and self.size == 3): # currently, randomstate only supported for 3x3x3
            # TODO randomstate not implemented
            return lambda: scramble_cube(self.size, moves=20)
        elif(self.scrambler == "minx"):
            # TODO implement non-cubic scramblers
            raise NotImplementedError("*minx scramblers not yet implemented")
        elif(self.scrambler == "cubic"):
            n_moves = {3: 20, 4: 40, 5: 60}
            return lambda: scramble_cube(self.size, moves=n_moves[self.size])
        else:
            raise NotImplementedError("Non-cubic scramblers not yet implemented")

    def getScramble(self):
        return self.getScrambler()()

    def __str__(self):
        return self.name
