from django.db import models
from apps.pc.models import *

class Store(models.Model):
    name = models.CharField('Store name', max_length=50)
    website = models.URLField('website url', max_length=500)
    logo_url = models.URLField('Logo url', max_length=500)

    cpu = models.ManyToManyField(Cpu, through='Store_cpu')
    gpu = models.ManyToManyField(Gpu, through='Store_gpu')
    board = models.ManyToManyField(Board, through='Store_board')
    ram = models.ManyToManyField(Ram, through='Store_ram')
    storage = models.ManyToManyField(Storage, through='Store_storage')
    psu = models.ManyToManyField(Psu, through='Store_psu')
    case = models.ManyToManyField(Case, through='Store_case')
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return "{}".format(self.name)

class Store_cpu(models.Model):
    id =  models.AutoField(primary_key=True)
    cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    url = models.URLField('Url', max_length=500)
    price = models.IntegerField('Price')
    is_available = models.BooleanField('Is Available', default=True)
    
    class Meta:
        verbose_name = 'CPU in Store'
        verbose_name_plural = 'CPUs in Store'
        ordering = ['cpu']

    def __str__(self):
        return "{} ({})".format(self.cpu, self.store)

class Store_gpu(models.Model):
    id =  models.AutoField(primary_key=True)
    gpu = models.ForeignKey(Gpu, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    url = models.URLField('Url', max_length=500)
    price = models.IntegerField('Price')
    is_available = models.BooleanField('Is Available', default=True)
    
    class Meta:
        verbose_name = 'GPU in Store'
        verbose_name_plural = 'GPUs in Store'
        ordering = ['gpu']

    def __str__(self):
        return "{} ({})".format(self.gpu, self.store)

class Store_board(models.Model):
    id =  models.AutoField(primary_key=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    url = models.URLField('Url', max_length=500)
    price = models.IntegerField('Price')
    is_available = models.BooleanField('Is Available', default=True)
    
    class Meta:
        verbose_name = 'Board in Store'
        verbose_name_plural = 'Boards in Store'
        ordering = ['board']

    def __str__(self):
        return "{} ({})".format(self.board, self.store)

class Store_ram(models.Model):
    id =  models.AutoField(primary_key=True)
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    url = models.URLField('Url', max_length=500)
    price = models.IntegerField('Price')
    is_available = models.BooleanField('Is Available', default=True)
    
    class Meta:
        verbose_name = 'RAM in Store'
        verbose_name_plural = 'RAMs in Store'
        ordering = ['ram']

    def __str__(self):
        return "{} ({})".format(self.ram, self.store)

class Store_storage(models.Model):
    id =  models.AutoField(primary_key=True)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    url = models.URLField('Url', max_length=500)
    price = models.IntegerField('Price')
    is_available = models.BooleanField('Is Available', default=True)
    
    class Meta:
        verbose_name = 'Storage in Store'
        verbose_name_plural = 'Storages in Store'
        ordering = ['storage']

    def __str__(self):
        return "{} ({})".format(self.storage, self.store)

class Store_psu(models.Model):
    id =  models.AutoField(primary_key=True)
    psu = models.ForeignKey(Psu, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    url = models.URLField('Url', max_length=500)
    price = models.IntegerField('Price')
    is_available = models.BooleanField('Is Available', default=True)
    
    class Meta:
        verbose_name = 'PSU in Store'
        verbose_name_plural = 'PSUs in Store'
        ordering = ['psu']

    def __str__(self):
        return "{} ({})".format(self.psu, self.store)

class Store_case(models.Model):
    id =  models.AutoField(primary_key=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    url = models.URLField('Url', max_length=500)
    price = models.IntegerField('Price')
    is_available = models.BooleanField('Is Available', default=True)
    
    class Meta:
        verbose_name = 'Case in Store'
        verbose_name_plural = 'Cases in Store'
        ordering = ['case']

    def __str__(self):
        return "{} ({})".format(self.case, self.store)