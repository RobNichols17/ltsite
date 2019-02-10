# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.conf import settings
from django.db import models


class Category(models.Model):
    catid = models.AutoField(db_column='catid', primary_key=True)  
    name = models.CharField(db_column='name', max_length=30, blank=True, null=True) 
    variety = models.CharField(db_column='variety', max_length=40, blank=True, null=True)
    description = models.CharField(db_column='description', max_length=75, blank=True, null=True)  
    
    def __str__(self):
        return self.name + ' - ' + self.variety
    
    class Meta:
        managed = True
        db_table = 'Category'

class Producer(models.Model):
    producerid = models.AutoField(db_column='producerid', primary_key=True)  
    name = models.CharField(db_column='name', max_length=45, blank=True, null=True)  
    state = models.CharField(db_column='state', max_length=2, blank=True, null=True)  
    country = models.CharField(db_column='country', max_length=40, blank=True, null=True)  

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Producer'

class Catalog(models.Model):
    catalogid = models.AutoField(db_column='catalogid', primary_key=True)  
    name = models.CharField(db_column='name', max_length=40, blank=True, null=True)  
    description = models.TextField(db_column='description', blank=True, null=True)  
    color = models.CharField(db_column='color', max_length=20, blank=True, null=True)
    tastingnotes = models.TextField(db_column='tastingnotes', blank=True, null=True)
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='categoryid', blank=True, null=True)  
    producerid = models.ForeignKey(Producer, models.DO_NOTHING, db_column='producerid', blank=True, null=True)  
    imgname = models.CharField(db_column='imgname',  max_length=100, blank=True, null=True) 
    catalog_img = models.ImageField(upload_to='bottles', blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Catalog'

class Inventory(models.Model):
    invid = models.AutoField(db_column='invid', primary_key=True)  
    quantity = models.IntegerField(db_column='quantity', blank=True, null=True)  
    catalogid = models.ForeignKey(Catalog, models.DO_NOTHING, db_column='catalogid', blank=True, null=True)  

    def __str__(self):
        return self.invid

    class Meta:
        managed = True
        db_table = 'Inventory'

