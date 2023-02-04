from django.db import models
import string , random
def gen_unique_code():
    length = 6
    while True:
        code = ''.join(random.choice(string.ascii_letters_.uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(default=False, null=False)
    votes_to_skip = models.IntegerField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)