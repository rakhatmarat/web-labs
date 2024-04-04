from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()
    category_id = models.IntegerField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'category': get_category(self.category_id),
            'description': self.description,
            'count': self.count
        }


def get_all_products():
    return Product.objects.all()


def get_all_categories():
    return Category.objects.all()


def get_category(cate_id):
    for category in get_all_categories():
        if cate_id == category.id:
            return category.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
