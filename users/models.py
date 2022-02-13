from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#MEVCUT USERIMIZIN OLDUĞU ABSTRACTUSER DAN İNHERİT ETTİK (TÜM ÖZELLİKLERİNİ ALDIK) AYNI ZAMANDA CUSTUMAZE YAPTIK(YENİ ÖZELLİKLER VERDİK)
#YENİ BİR USER CLASSI OLUSTURDUK
#default gelen userı degiştirmiş olduk
class User(AbstractUser):
   
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    bio =models.TextField()
