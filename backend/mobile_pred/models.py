from django.db import models

class MobilePhone(models.Model):
    battery_power = models.IntegerField(help_text='Total energy a battery can store in mAh')
    blue = models.IntegerField(help_text='Has Bluetooth or not')
    clock_speed = models.FloatField(help_text='Speed at which microprocessor executes instructions')
    dual_sim = models.IntegerField(help_text='Has dual sim support or not')
    fc = models.IntegerField(help_text='Front Camera megapixels')
    four_g = models.IntegerField(help_text='Has 4G or not')
    int_memory = models.IntegerField(help_text='Internal Memory in Gigabytes')
    m_dep = models.FloatField(help_text='Mobile Depth in cm')
    mobile_wt = models.IntegerField(help_text='Weight of mobile phone')
    n_cores = models.IntegerField(help_text='Number of cores of processor')
    pc = models.IntegerField(help_text='Primary Camera megapixels')
    px_height = models.IntegerField(help_text='Pixel Resolution Height')
    px_width = models.IntegerField(help_text='Pixel Resolution Width')
    ram = models.IntegerField(help_text='Random Access Memory in Megabytes')
    sc_h = models.FloatField(help_text='Screen Height of mobile in cm')
    sc_w = models.FloatField(help_text='Screen Width of mobile in cm')
    talk_time = models.IntegerField(help_text='Longest time that a single battery charge will last')
    three_g = models.IntegerField(help_text='Has 3G or not')
    touch_screen = models.IntegerField(help_text='Has touch screen or not')
    wifi = models.IntegerField(help_text='Has wifi or not')
    price_range = models.IntegerField(help_text='Price range category of the mobile phone', null=True, blank=True)

    def __str__(self):
        return f"Mobile Phone {self.id} - Price Range: {self.price_range}"
