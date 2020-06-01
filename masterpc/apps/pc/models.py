from django.db import models
from .choices import *
from apps.store.models import *

class Manufacturer(models.Model):
    name = models.CharField('Manufacturer name', max_length=30)
    logo_url = models.URLField('Logo url', max_length=500)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Cpu(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    serie = models.CharField('Serie', max_length=20)
    model = models.CharField('Model', max_length=20)
    cores = models.IntegerField('Number of Cores', default=4)
    threads = models.IntegerField('Number of Threads', default=8)
    base_clock = models.DecimalField('Base Clock (GHz)', max_digits=4, decimal_places=2, default=3.2)
    boost_clock = models.DecimalField('Max Boost Clock (GHz)', max_digits=4, decimal_places=2, default=3.6)
    tdp = models.IntegerField('TDP (W)', default=65)
    max_temps = models.IntegerField('Max Temps (C)', default=95)
    socket = models.CharField('Socket type', max_length=10, choices=Socket.choices)
    integrated_graphics = models.BooleanField('Integrated Graphics', default=False)
    pcie_version = models.DecimalField('PCI Express Version', max_digits=2, decimal_places=1, default=4.0)
    ram_type = models.CharField('RAM Type', max_length=4, default='DDR4')
    ram_speed = models.IntegerField('RAM Speed (MHz)', choices=RamSpeed.choices, default=RamSpeed.O3000)
    ram_max_size = models.IntegerField('RAM Max Size (GB)', choices=RamSize.choices, default=RamSize.O64)
    manufacturer_website = models.URLField('Manufacturer website', max_length=500)
    img1_url = models.URLField('Image 1 url', max_length=500)
    img2_url = models.URLField('Image 2 url', max_length=500, blank=True, null=True)
    img3_url = models.URLField('Image 3 url', max_length=500, blank=True, null=True)
    img4_url = models.URLField('Image 4 url', max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'CPU'
        verbose_name_plural = 'CPUs'

    def __str__(self):
        return "{} {} {}".format(self.manufacturer.name, self.serie, self.model)

class Gpu(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    serie = models.CharField('Serie', max_length=30)
    model = models.CharField('Model', max_length=40)
    base_clock =  models.IntegerField('GPU Clock Speed (MHz)', default=1400)
    boost_clock =  models.IntegerField('GPU Turbo (MHz)', default=1700)
    tdp = models.IntegerField('TDP (W)', default=100)
    pcie_version = models.DecimalField('PCI Express Version', max_digits=2, decimal_places=1, default=4.0)
    vram_size = models.IntegerField('VRAM size (GB)', default=4)
    memory_speed =  models.IntegerField('GPU Memory Speed (MHz)', default=1500)
    max_memory_bandwidth = models.IntegerField('Max Memory Bandwidth (GB/s)', default=190)
    tflops = models.DecimalField('TFLOPS', max_digits=4, decimal_places=2, default=4.5)
    # pixel_rate = models.DecimalField('Pixel Rate (GPixel/s)', max_digits=4, decimal_places=2, default=55.0)
    manufacturer_website = models.URLField('Manufacturer website', max_length=500)
    img1_url = models.URLField('Image 1 url', max_length=500)
    img2_url = models.URLField('Image 2 url', max_length=500, blank=True, null=True)
    img3_url = models.URLField('Image 3 url', max_length=500, blank=True, null=True)
    img4_url = models.URLField('Image 4 url', max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'GPU'
        verbose_name_plural = 'GPUs'

    def __str__(self):
        return "{} {} {} ({}GB)".format(self.manufacturer.name, self.serie, self.model, self.vram_size)

class Board(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    serie = models.CharField('Serie', max_length=20)
    model = models.CharField('Model', max_length=20)
    socket = models.CharField('Socket type', max_length=10, choices=Socket.choices)
    wifi = models.BooleanField('Integrated Wi-Fi', default=False)
    dual_bios = models.BooleanField('Dual BIOS', default=False)
    pcie_version = models.DecimalField('PCI Express Version', max_digits=2, decimal_places=1, default=4.0)
    ram_slots = models.IntegerField('RAM Slots', default=4)
    ram_type = models.CharField('RAM Type', max_length=4, default='DDR4')
    ram_speed = models.IntegerField('RAM Speed (MHz)', choices=RamSpeed.choices, default=RamSpeed.O3000)
    ram_speed_oc = models.IntegerField('RAM Speed OC (MHz)', choices=RamSpeed.choices, default=RamSpeed.O3600)
    ram_max_size = models.IntegerField('RAM Max Size (GB)', choices=RamSize.choices, default=RamSize.O64)
    usb2_ports = models.IntegerField('USB 2.0 Ports', default=4)
    usb3_ports = models.IntegerField('USB 3.0 Ports', default=4)
    fan_headers = models.IntegerField('Fan Headers', default=2)
    manufacturer_website = models.URLField('Manufacturer website', max_length=500)
    img1_url = models.URLField('Image 1 url', max_length=500)
    img2_url = models.URLField('Image 2 url', max_length=500, blank=True, null=True)
    img3_url = models.URLField('Image 3 url', max_length=500, blank=True, null=True)
    img4_url = models.URLField('Image 4 url', max_length=500, blank=True, null=True)

    def __str__(self):
        return "{} {} {}".format(self.manufacturer.name, self.serie, self.model)


class Ram(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    serie = models.CharField('Serie', max_length=20)
    model = models.CharField('Model', max_length=30)
    memory_type = models.CharField('Type', max_length=4, default='DDR4')
    speed = models.IntegerField('Speed', choices=RamSpeed.choices, default=RamSpeed.O3000)
    size = models.IntegerField('Total Size', choices=RamSize.choices, default=RamSize.O8)
    size_kit = models.CharField('Size Kit', max_length=4, choices=SIZE_KIT_CHOICES, default='8x1')
    # latency = models.CharField('Latency', max_length=20)
    manufacturer_website = models.URLField('Manufacturer website', max_length=500)
    img1_url = models.URLField('Image 1 url', max_length=500)
    img2_url = models.URLField('Image 2 url', max_length=500, blank=True, null=True)
    img3_url = models.URLField('Image 3 url', max_length=500, blank=True, null=True)
    img4_url = models.URLField('Image 4 url', max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'RAM'
        verbose_name_plural = 'RAMs'

    def __str__(self):
        return "{} {} {} - {} {}".format(self.manufacturer.name, self.serie, self.model, self.get_size_kit_display(), self.get_speed_display())

class Storage(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    serie = models.CharField('Serie', max_length=20)
    model = models.CharField('Model', max_length=20)
    storage_type = models.CharField('Type', max_length=20, choices=StorageType.choices, default=StorageType.SSD)
    capacity = models.IntegerField('Capacity', choices=StorageSize.choices, default=StorageSize.O240)
    form_factor = models.CharField('Form Factor', max_length=20, choices=StorageFormFactor.choices, default=StorageFormFactor.O2)
    manufacturer_website = models.URLField('Manufacturer website', max_length=500)
    img1_url = models.URLField('Image 1 url', max_length=500)
    img2_url = models.URLField('Image 2 url', max_length=500, blank=True, null=True)
    img3_url = models.URLField('Image 3 url', max_length=500, blank=True, null=True)
    img4_url = models.URLField('Image 4 url', max_length=500, blank=True, null=True)

    def __str__(self):
        return "{} {} {} {} {}".format(self.manufacturer.name, self.serie, self.model, self.capacity, self.storage_type)


class Psu(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    serie = models.CharField('Serie', max_length=20)
    model = models.CharField('Model', max_length=20)
    watts = models.IntegerField('Watts (W)', choices=Watts.choices, default=Watts.O500)
    certified = models.CharField('Certified', max_length=20, choices=Certified.choices, default=Certified.STANDARD)
    modular = models.CharField('Modular', max_length=20, choices=Modular.choices, default=Modular.NO_MODULAR)
    manufacturer_website = models.URLField('Manufacturer website', max_length=500)
    img1_url = models.URLField('Image 1 url', max_length=500)
    img2_url = models.URLField('Image 2 url', max_length=500, blank=True, null=True)
    img3_url = models.URLField('Image 3 url', max_length=500, blank=True, null=True)
    img4_url = models.URLField('Image 4 url', max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'PSU'
        verbose_name_plural = 'PSUs'

    def __str__(self):
        return "{} {} {} 80+ {}".format(self.manufacturer.name, self.serie, self.model, self.get_certified_display())

class Case(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    serie = models.CharField('Serie', max_length=20)
    model = models.CharField('Model', max_length=20)
    case_type = models.CharField('Board Size', max_length=20, choices=CaseType.choices, default=CaseType.MID_TOWER)
    board_size = models.CharField('Board Size', max_length=10, choices=BoardSize.choices, default=BoardSize.ATX)
    usb2_ports = models.IntegerField('USB 2.0 Ports', default=0)
    usb3_ports = models.IntegerField('USB 3.0 Ports', default=2)
    manufacturer_website = models.URLField('Manufacturer website', max_length=500)
    img1_url = models.URLField('Image 1 url', max_length=500)
    img2_url = models.URLField('Image 2 url', max_length=500, blank=True, null=True)
    img3_url = models.URLField('Image 3 url', max_length=500, blank=True, null=True)
    img4_url = models.URLField('Image 4 url', max_length=500, blank=True, null=True)

    def __str__(self):
        return "{} {} {}".format(self.manufacturer.name, self.serie, self.model)