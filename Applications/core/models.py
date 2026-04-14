from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    ruc = models.CharField(max_length=20, unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    verified = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class GeneratedFood(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    ruc = models.CharField(max_length=20, unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    generated_food = models.ForeignKey(GeneratedFood, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    available_from = models.DateTimeField(blank=True, null=True)
    available_until = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Items_Publication(models.Model):
    id = models.AutoField(primary_key=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Schedules(models.Model):
    id = models.AutoField(primary_key=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    total_people = models.IntegerField(blank=True, null=True)
    pickup_time = models.DateTimeField(auto_now_add=True)
    delivery_time = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Schedule for {self.publication.title}"

class Delivery(models.Model):
    id = models.AutoField(primary_key=True)
    schedule = models.ForeignKey(Schedules, on_delete=models.CASCADE)  
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    delivery_time = models.DateTimeField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Delivery for {self.schedule.publication.title}"
    
class Qualification(models.Model):
    id = models.AutoField(primary_key=True)
    schedule = models.ForeignKey(Schedules, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, blank=True, null=True)
    type_author = models.CharField(max_length=50, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Qualification for {self.schedule.publication.title}"