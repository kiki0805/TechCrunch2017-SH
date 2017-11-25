from django.contrib.auth.models import User
from django.db import models
from tags.models import Tag
from mode.models import Mode

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    tags = models.ManyToManyField(Tag)
    modes = models.ManyToManyField(Mode)

    def __unicode__(self):
        return self.user.username

class UserStatus(models.Model):
    user = models.ForeignKey(User)
    location = models.CharField()
    count = models.IntegerField(default=1)

    def __unicode__(self):
        return "%s:%s" % self.user.username, self.location

    def update_count(self):
        self.count += 1
        self.save()
