from django.db import models
from django.urls import reverse


class Found_input(models.Model):
    category = models.CharField(max_length=32, verbose_name="분류")
    name = models.CharField(max_length=32, verbose_name="물품명",)
    location = models.CharField(max_length=255, verbose_name="습득위치")
    date = models.CharField(max_length=30, verbose_name="습득날짜")
    image = models.ImageField(upload_to='images/found/%Y/%m', verbose_name="물품사진", help_text="파일 형식은 jpg 또는 png로, 사이즈는 가로 1,240px, 세로 930px 이상으로 올려주세요.")
    contact = models.CharField(max_length=15, verbose_name="연락처")
    description = models.TextField(verbose_name="상세설명")
    registered_date = models.DateTimeField(verbose_name="등록시간", auto_now_add=True)



    class Meta:
        db_table = "Input_Found_list"
        verbose_name = "습득물"
        verbose_name_plural = "습득물들"
        ordering = ('-registered_date',)

    def __str__(self):
        return self.name




class Lost_input(models.Model):
    category = models.CharField(max_length=32, verbose_name="분류")
    name = models.CharField(max_length=32, verbose_name="물품명")
    location = models.CharField(max_length=255, verbose_name="분실위치")
    date = models.CharField(max_length=32, verbose_name="분실날짜", )
    money = models.CharField(max_length=255, verbose_name="사례금", )
    image = models.ImageField(upload_to='images/lost/%Y/%m', )
    contact = models.CharField(max_length=13, verbose_name="연락처")
    description = models.TextField(verbose_name="상세설명")
    registered_date = models.DateTimeField(verbose_name="등록시간", auto_now_add=True)



    class Meta:
        db_table = "Input_Lost_list"
        verbose_name = "분실물"
        verbose_name_plural = "분실물들"
        ordering = ('-registered_date',)

    def __str__(self):
        return self.name
