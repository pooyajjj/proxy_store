from django.db import models



class products(models.Model):
    name = models.CharField(max_length=225)
    descraption = models.CharField(max_length=225)
    # id = models.SmallIntegerField(unique=True, primary_key=True)
    is_stock = models.BooleanField()
    slug = models.SlugField(unique=True, max_length=225)
    price = models.SmallIntegerField()
    img = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)


    class Meta():
        ordering = ('name',)



    def __str__(self):
        return self.name