from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name ="عنوان")
    text = models.TextField(verbose_name ="متن")
    photo = models.ImageField(upload_to="news", verbose_name ="عکس")
    publish = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = "مطلب"
        verbose_name_plural = "مطالب"


    def __str__(self):
        return self.title

    



class ContactMessage(models.Model):
    email = models.EmailField(verbose_name="ایمیل")
    message = models.TextField(verbose_name="پیام")
    subject = models.CharField(max_length=255, verbose_name="موضوع")


    class Meta:
        verbose_name = "صندوق پیام"
        verbose_name_plural = "صندوق پیام ها"

    def __str__(self):
        return self.subject


class Slider(models.Model):
    title = models.TextField()
    photo = models.ImageField(upload_to="slider")


    class Meta:
            verbose_name = "اسلایدر عکس"
            verbose_name_plural = "اسلایدر عکس ها"
    def __str__(self):
        return self.title
