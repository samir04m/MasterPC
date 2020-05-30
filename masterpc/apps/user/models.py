from django.db import models
from django.contrib.auth.models import User
from apps.store.models import *

class Pc(models.Model):
    name = models.CharField('PC name', max_length=50)
    budget = models.IntegerField('Budget', blank=True, null=True)
    create_at = models.DateTimeField('Create at', auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, related_name='pcs', on_delete=models.CASCADE)

    cpu = models.ManyToManyField(Store_cpu, through='Pc_cpu')
    gpu = models.ManyToManyField(Store_gpu, through='Pc_gpu')
    board = models.ManyToManyField(Store_board, through='Pc_board')
    ram = models.ManyToManyField(Store_ram, through='Pc_ram')
    storage = models.ManyToManyField(Store_storage, through='Pc_storage')
    psu = models.ManyToManyField(Store_psu, through='Pc_psu')
    case = models.ManyToManyField(Store_case, through='Pc_case')
    
    class Meta:
        verbose_name = 'PC'
        verbose_name_plural = 'PCs'

    def __str__(self):
        return "{} \"{}\"".format(self.user.username, self.name)

class Pc_cpu(models.Model):
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    store_cpu = models.ForeignKey(Store_cpu, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PC CPU'
        verbose_name_plural = 'PC CPUs'

    def __str__(self):
        return "{} - {} ({})".format(self.pc, self.store_cpu.cpu, self.store_cpu.store)

class Pc_gpu(models.Model):
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    store_gpu = models.ForeignKey(Store_gpu, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PC GPU'
        verbose_name_plural = 'PC GPUs'
        # ordering = ['gpu']

    def __str__(self):
        return "{} - {} ({})".format(self.pc, self.store_gpu.gpu, self.store_cpu.store)

class Pc_board(models.Model):
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    store_board = models.ForeignKey(Store_board, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PC Board'
        verbose_name_plural = 'PC Boards'
        # ordering = ['board']

    def __str__(self):
        return "{} - {} ({})".format(self.pc, self.store_board.board, self.store_board.store)

class Pc_ram(models.Model):
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    store_ram = models.ForeignKey(Store_ram, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PC RAM'
        verbose_name_plural = 'PC RAMs'
        # ordering = ['ram']

    def __str__(self):
        return "{} - {} ({})".format(self.pc, self.store_ram.ram, self.store_ram.store)

class Pc_storage(models.Model):
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    store_storage = models.ForeignKey(Store_storage, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PC Storage'
        verbose_name_plural = 'PC Storages'
        # ordering = ['storage']

    def __str__(self):
        return "{} - {} ({})".format(self.pc, self.store_storage.storage, self.store_storage.store)

class Pc_psu(models.Model):
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    store_psu = models.ForeignKey(Store_psu, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PC PSU'
        verbose_name_plural = 'PC PSUs'
        # ordering = ['psu']

    def __str__(self):
        return "{} - {} ({})".format(self.pc, self.store_psu.psu, self.store_psu.store)

class Pc_case(models.Model):
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE)
    store_case = models.ForeignKey(Store_case, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'PC Case'
        verbose_name_plural = 'PC Cases'
        # ordering = ['case']

    def __str__(self):
        return "{} - {} ({})".format(self.pc, self.store_case.case, self.store_case.store)