from django.db import models
from django.db.models import Sum
from django.contrib import messages
import logging
from django_middleware_global_request import get_request

logger = logging.getLogger("app")


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    friendly_name = models.CharField(max_length=255)

    def __str__(self):
        return "FN[{}]".format(self.friendly_name)

    class Meta:
        abstract = True


class Club(BaseModel):
    budget = models.FloatField()

    def __str__(self):
        return "FN [{}] Available Budget [{}]".format(self.friendly_name, self.budget - self.committed_budget)

    @property
    def committed_budget(self):
        accum = 0
        for model in [Player, Manager]:
            result = model.objects.filter(club=self.id).aggregate(Sum("salary"))["salary__sum"] or 0
            if result is None:
                continue
            accum = accum + result

        return accum


class ClubEmployee(BaseModel):
    salary = models.FloatField()
    club = models.ForeignKey(Club, default=None, blank=True, null=True, on_delete=models.SET_NULL)

    def __init__(self, *args, **kwargs):
        super(ClubEmployee, self).__init__(*args, **kwargs)
        self.original_salary = self.salary
        self.original_club = self.club

    def save(self, *args, **kwargs):
        can_be_paid, remaining_budget = self.salary_can_be_paid()
        if can_be_paid:
            super(ClubEmployee, self).save(*args, **kwargs)
        else:
            messages.set_level(get_request(), messages.ERROR)
            messages.add_message(get_request(), messages.ERROR, 'NOT Saved. Club remaining budget [{}] is not enough for hiring this employee with salary [{}]'.format(remaining_budget, self.salary))
            self.club = None
            self.friendly_name = None
            self.salary = 0
            return False

    def salary_can_be_paid(self):
        if self.club is None:
            return True, 0

        club = Club.objects.get(pk=self.club.id)
        remaining_budget = club.budget - club.committed_budget
        if self.original_club.id == self.club.id:
            remaining_budget = remaining_budget + self.original_salary
        if (remaining_budget - self.salary) >= 0:
            return True, remaining_budget
        return False, remaining_budget

    class Meta:
        abstract = True


class Player(ClubEmployee):
    pass


class Manager(ClubEmployee):
    pass
