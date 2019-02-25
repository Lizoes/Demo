from django.db import models

# Create your models here.


class Business(models.Model):
    caption=models.CharField(max_length=32)
    code=models.CharField(max_length=32)


class Host(models.Model):
    CHOICES=(
        ("M","男"),
        ("W","女"),
        ("S","保密")
    )
    nid=models.AutoField(primary_key=True)
    hostname=models.CharField(max_length=32,db_index=True)
    ip=models.GenericIPAddressField(protocol="IPV4",db_index=True)
    port=models.IntegerField()
    bus=models.ForeignKey(to="Business",to_field="id",on_delete=models.CASCADE)
    choices=models.CharField(max_length=1,choices=CHOICES,default="S")
    #other=models.IntegerField(default=0)
    ctime=models.DateTimeField(auto_now_add=True,null=True)
    updatetime=models.DateTimeField(auto_now=True,null=True)