from django.db import models

# Create your models here.


class Agents(models.Model):
    is_available = models.IntegerField()
    available_since = models.CharField(max_length=20)
    roles = models.CharField(max_length=200)

    def __str__(self):
        return f'''Agent : {self.id}\tAvailable : {'True' if self.is_available else 'False'}'''

    def allDetail(self):
        detail = {}
        detail['Agent ID'] = self.id
        detail['Available'] = 'True' if self.is_available else 'False'
        detail['Available Since'] = self.available_since
        detail['Roles'] = self.roles.replace(' ', ' | ')
        return detail

    class Meta:
        db_table = 'Agents'
