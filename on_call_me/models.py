from django.db import models


class TeamMember(models.Model):
    u_name = models.CharField(max_length=8, primary_key=True)
    full_name = models.CharField(max_length=50)
    role = models.CharField(max_length=20)


class OnCallPeriod(models.Model):

    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    week_ending = models.DateField('week ending')
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    hours = models.IntegerField(default=0)
