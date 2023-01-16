from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    phone_number = models.IntegerField(10)
    email_address=models.EmailField()
    password=models.CharField(max_length=50)

    def register(self):
        self.save()
    @staticmethod
    def get_customer_by_email_address(email_address):
        try:
            return Customer.objects.get(email_address=email_address)
        except:
            return False

    def isExist(self):
        if Customer.objects.filter(email_address=self.email_address):
            return True
        else:
            return False