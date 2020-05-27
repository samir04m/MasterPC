from django.db import models
from django.utils.translation import gettext_lazy as _

class Socket(models.TextChoices):
    AM4 = 'AM4'
    TR4 = 'TR4'
    LGA1151 = 'LGA 1151'

class RamSpeed(models.IntegerChoices):
    O2400 = 2400, '2400 MHz'
    O2600 = 2600, '2600 MHz'
    O2666 = 2666, '2666 MHz'
    O2933 = 2933, '2933 MHz'
    O3000 = 3000, '3000 MHz'
    O3200 = 3200, '3200 MHz'
    O3333 = 3333, '3333 MHz'
    O3466 = 3466, '3466 MHz'
    O3600 = 3600, '3600 MHz'
    O3800 = 3800, '3800 MHz'
    O4000 = 4000, '4000 MHz'
    O4266 = 4266, '4266 MHz'

class RamSize(models.IntegerChoices):
    O4 = 4, '4 GB'
    O8 = 8, '8 GB'
    O16 = 16, '16 GB'
    O32 = 32, '32 GB'
    O64 = 64, '64 GB'
    O128 = 128, '128 GB'

class StorageSize(models.IntegerChoices):
    O128 = 128, '128 GB'
    O240 = 240, '240 GB'
    O480 = 480, '480 GB'
    O512 = 512, '512 GB'
    O960 = 960, '960 GB'
    O1 = 1024, '1 TB'
    O2 = 2048, '2 TB'
    O3 = 3072, '3 TB'
    O4 = 4096, '4 TB'

class StorageType(models.TextChoices):
    SSDM2 = 'M.2 SSD', _('M.2 SSD')
    SSD = 'SSD', _('SSD')
    HDD5 = 'HDD 5.4K RPM', _('HDD 5.4K RPM')
    HDD7 = 'HDD 7.2K RPM', _('HDD 7.2K RPM')
    HDD10 = 'HDD 10K RPM', _('HDD 10K RPM')

class StorageFormFactor(models.TextChoices):
    M2242 = 'M.2 2242', _('M.2 2242')
    M2260 = 'M.2 2260', _('M.2 2260')
    M2280 = 'M.2 2280', _('M.2 2280')
    M22110 = 'M.2 22110', _('M.2 22110')
    O2 = '2.5"', _('2.5"')
    O3 = '3.5"', _('3.5"')

class Watts(models.IntegerChoices):
    O400 = 400, '400W'
    O450 = 450, '450W'
    O500 = 500, '500W'
    O550 = 550, '550W'
    O600 = 600, '600W'
    O650 = 650, '650W'
    O700 = 700, '700W'
    O750 = 750, '750W'

class Certified(models.TextChoices):
    STANDARD = 'Standard'
    BRONZE = 'Bronze'
    SILVER = 'Silver'
    GOLD = 'Gold'
    PLATINUM = 'Platinum'
    TITANIUM = 'Titanium'

class Modular(models.TextChoices):
    NO_MODULAR = 'No Modular'
    SEMI_MODULAR = 'Semi Modular'
    FULL_MODULAR = 'Full Modular'

class CaseType(models.TextChoices):
    FULL_TOWER = 'Full Tower'
    MID_TOWER = 'Mid Tower'
    MINI_TOWER = 'Mini Tower'

class BoardSize(models.TextChoices):
    ATX = 'ATX'
    MICRO_ATX = 'Micro ATX'
    MINI_ITX = 'Mini ITX'

SIZE_KIT_CHOICES = [('4x1','4GB'),('4x2','8GB (2x4GB)'),('8x1','8GB'),
    ('16x1','16GB'),('4x4','16GB (4x4GB)'),('8x2','16GB (2x8GB)'),
    ('32x1','32GB'),('8x4','32GB (4x8GB)'),('16x2','32GB (2x16GB)'),
    ('16x4','64GB (4x16GB)'),('32x2','64GB (2x32GB)'),('32x4','128GB (4x32GB)')]
