from django.db import models

# Create your models here.


class cinema(models.Model):
    names = models.CharField("影院名称",max_length=256)
    cinemaCode = models.CharField('影城编码', max_length=256,primary_key=True)
    systemName = models.CharField('票务系统',max_length=50,null=True)
    maoyanId = models.IntegerField('猫眼id',null=True)
    taopiaopiaoId = models.IntegerField('淘票票id',null=True,default=None)
    readme = models.TextField("说明",default='not thing')

    class Meta:
        verbose_name = '影城名称'
        verbose_name_plural = '影城名称'
        ordering = ['names']  # 按照哪个栏目排序

    def __str__(self):
        return self.names
