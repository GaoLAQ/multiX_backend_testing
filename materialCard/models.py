from django.db import models

# Create your models here.

class MaterialCard(models.Model):
    class Material(models.TextChoices):
        AA5754 = 'AA5754','AA5754'
        AA6082 = 'AA6082','AA6082'
        AA7075 = 'AA7075','AA7075'
    class Anisotropy(models.TextChoices):
        ISOTROPIC = 'isotropic','isotropic'
        ORTHOTROPIC = 'orthotropic','orthotropic'

    title = models.CharField(max_length=120)
    materialType = models.CharField(max_length=50, choices=Material.choices, default='') 
    description = models.TextField()
    anisotropic = models.CharField(max_length=50, choices=Anisotropy.choices, default='') 
    uploadImage = models.FileField(upload_to='logos', default='logos/logo.png')
    youngModulus = models.IntegerField(default=0)
    possionRatio = models.IntegerField(default=0)

    def _str_(self):
        return self.title