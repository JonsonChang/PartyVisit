# coding=UTF-8

from django.db import models


PEOPLE_AUTH_CHOICES = (
    (0, '民眾'),
    (1, '義工'),
    (2, '隊長'),
    (99, '管理者'),
)    


PEOPLE_STATE_CHOICES = (
    (0, '無狀態'),
    (1, '拒決'),
    (2, '認同'),
    (9, '已入黨'),
)    
PEOPLE_SEX_CHOICES = (
    (0, '女'),
    (1, '男'),
)
PEOPLE_SCHOOL_STATUS_CHOICES = (
    (0, '畢業'),
    (1, '就讀'),
)
PEOPLE_EDU_CHOICES = (
    (1, '國小'),
    (2, '國中'),
    (3, '高中/職'),
    (4, '專科'),
    (5, '學士'),
    (6, '碩士'),
    (7, '博士'),
)
PEOPLE_RELIGION_CHOICES = (
    (1, '佛教'),
    (2, '回教'),
    (3, '道教'),
    (4, '天主教'),
    (5, '基督教'),
    (6, '一貫道'),
    (7, '無'),
    (8, '其他'),
)
PEOPLE_IN_OTHER_PARTY_CHOICES = (
    (0, '未曾加入其他政黨'),
    (1, '增加入'),
)

class address(models.Model):
    store = models.CharField(verbose_name="店家名", max_length=255, blank=True)
    city = models.CharField(verbose_name="縣/市", max_length=255)
    area = models.CharField(verbose_name="區",max_length=255)
    vil = models.CharField(verbose_name="里/村", max_length=255, blank=True)
    nei = models.CharField(verbose_name="鄰",max_length=255, blank=True)
    rd = models.CharField(verbose_name="路/街",max_length=255, blank=True)
    seg = models.CharField(verbose_name="段",max_length=255, blank=True)
    lane = models.CharField(verbose_name="巷",max_length=255, blank=True)
    aller = models.CharField(verbose_name="弄",max_length=255, blank=True)
    num = models.CharField(verbose_name="號",max_length=255, blank=True)
    f = models.CharField(verbose_name="樓",max_length=255, blank=True)

    def __unicode__(self):
        return self.city + self.area + self.vil +self.nei +"鄰".decode('utf-8')+self.rd+self.seg+"段".decode('utf-8')+self.lane+"巷".decode('utf-8')+self.aller+"弄".decode('utf-8')+self.num+"號".decode('utf-8')+self.f+"樓".decode('utf-8')
#        return self.city + self.area + self.vil +self.nei+"鄰".decode('utf-8') +self.rd+self.seg+self.lane+self.aller+self.num+self.f
#        return "abcde"

class history(models.Model):
    address = models.ForeignKey(address, verbose_name="地址")
    visit_date = models.DateField(verbose_name="拜訪日期",auto_now_add=True)
    record = models.TextField(verbose_name="記錄")   
         
class people(models.Model):
# todo    auth_id    權限設定  
    address = models.ForeignKey(address, verbose_name="地址")
    is_del = models.BooleanField(verbose_name="停用", default=False)  
    auth = models.IntegerField(verbose_name="權限", choices=PEOPLE_AUTH_CHOICES, default=0)
    state = models.IntegerField(verbose_name="認同狀態",choices=PEOPLE_STATE_CHOICES, default=0)
    password = models.CharField(verbose_name="密碼",max_length=255, default="123456789")
    name = models.CharField(verbose_name="名字",max_length=255, blank=False, null = False)
    user_id = models.CharField(verbose_name="身份證字號",max_length=10,blank=True,unique=True)
    sex = models.IntegerField(verbose_name="性別",choices=PEOPLE_SEX_CHOICES, default=0)
    birthday = models.DateField(verbose_name="生日",blank=True)               
#    introducer = models.ForeignKey("self", null=True,verbose_name="介紹人")
    introducer = models.CharField(verbose_name="介紹人", max_length=255, blank=False, default="")
# #    introducer_phone        
    tel_office = models.CharField(verbose_name="公司電話",max_length=255, blank=True)
    tel_home = models.CharField(verbose_name="住家電話",max_length=255, blank=True)
    tel_mobile = models.CharField(verbose_name="手機",max_length=255, blank=True)
    email = models.EmailField(verbose_name="Email",max_length=255, blank=True)
    edu = models.IntegerField(verbose_name="學歷",choices=PEOPLE_EDU_CHOICES, default=0)
    school_status = models.IntegerField(verbose_name="就讀畢業",choices=PEOPLE_SCHOOL_STATUS_CHOICES, default=0)
    school = models.CharField(verbose_name="學校",max_length=255, blank=True)              
    major = models.CharField(verbose_name="科系",max_length=255, blank=True)
    company = models.CharField(verbose_name="公司名稱",max_length=255, blank=True)
    title = models.CharField(verbose_name="職稱",max_length=255, blank=True)
    religion = models.IntegerField(verbose_name="宗教信仰",choices=PEOPLE_RELIGION_CHOICES, default=0)
    is_other_political_party = models.IntegerField(verbose_name="是否參加過其他政黨",choices=PEOPLE_IN_OTHER_PARTY_CHOICES, default=0)
    political_party = models.CharField(verbose_name="政黨名稱",max_length=255, blank=True)
    def __unicode__(self):
        return self.name


	
