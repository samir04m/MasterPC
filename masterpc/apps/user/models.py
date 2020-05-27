from django.db import models
from django.contrib.auth.models import User
from apps.pc.models import *

class Pc(models.Model):
    name = models.CharField('PC name', max_length=50)
    budget = models.IntegerField('Budget', blank=True, null=True)
    create_at = models.DateTimeField('Create at', auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, related_name='pcs', on_delete=models.CASCADE)

    cpu = models.ManyToManyField(Cpu, through='Pc_cpu')
    gpu = models.ManyToManyField(Gpu, through='Pc_gpu')
    board = models.ManyToManyField(Board, through='Pc_board')
    ram = models.ManyToManyField(Ram, through='Pc_ram')
    storage = models.ManyToManyField(Storage, through='Pc_storage')
    psu = models.ManyToManyField(Psu, through='Pc_psu')
    case = models.ManyToManyField(Case, through='Pc_case')
    
    class Meta:
        verbose_name = 'PC'
        verbose_name_plural = 'PCs'

    def __str__(self):
        return "{} - {}".format(self.user.username, self.name)

class Pc_cpu(models.Model):
    cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PC CPU'
        verbose_name_plural = 'PC CPUs'
        ordering = ['cpu']

    def __str__(self):
        return "{} ({})".format(self.cpu, self.pc)

class Pc_gpu(models.Model):
    gpu = models.ForeignKey(Gpu, on_delete=models.CASCADE)
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PC GPU'
        verbose_name_plural = 'PC GPUs'
        ordering = ['gpu']

    def __str__(self):
        return "{} ({})".format(self.gpu, self.pc)

class Pc_board(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PC Board'
        verbose_name_plural = 'PC Boards'
        ordering = ['board']

    def __str__(self):
        return "{} ({})".format(self.board, self.pc)

class Pc_ram(models.Model):
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PC RAM'
        verbose_name_plural = 'PC RAMs'
        ordering = ['ram']

    def __str__(self):
        return "{} ({})".format(self.ram, self.pc)

class Pc_storage(models.Model):
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PC Storage'
        verbose_name_plural = 'PC Storages'
        ordering = ['storage']

    def __str__(self):
        return "{} ({})".format(self.storage, self.pc)

class Pc_psu(models.Model):
    psu = models.ForeignKey(Psu, on_delete=models.CASCADE)
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PC PSU'
        verbose_name_plural = 'PC PSUs'
        ordering = ['psu']

    def __str__(self):
        return "{} ({})".format(self.psu, self.pc)

class Pc_case(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PC Case'
        verbose_name_plural = 'PC Cases'
        ordering = ['case']

    def __str__(self):
        return "{} ({})".format(self.case, self.pc)