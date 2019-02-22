
class Recipe(models.Model):
    recipeid = models.AutoField(db_column='recipeid', primary_key=True)  
    name = models.IntegerField(db_column='name', blank=True, null=True)  
    description = models.TextField(db_column='description', blank=True, null=True)  

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Recipe'

class Ingredient(models.Model):
    ingredientid = models.AutoField(db_column='ingredientid', primary_key=True)  
    recipeid = models.ForeignKey(Recipe, models.PROTECT, db_column='recipeid',
                                 blank=False, null=True)  
    catalogid = models.ForeignKey(Catalog, models.PROTECT, db_column='catalogid', blank=True, null=True)  

    def __str__(self):
        return self.recipeid

    class Meta:
        managed = True
        db_table = 'Ingredient'
