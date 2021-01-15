from django.db import models

# Create your models here.

class Customer(models.Model):
    fname =models.CharField(max_length=50,blank= False,default='',null=True )
    oname =models.CharField(max_length=50,blank= False,default='',null=True )
    emp_id =models.CharField(max_length=50,blank= False,default='',null=True )
    mob = models.CharField(max_length=15,blank= False,default='',null=True )
    email = models.EmailField(max_length=254,blank= False,default='',null=True )
    image = models.FileField(upload_to='uploads/ids/',blank= False,default='',null=True )
    password = models.CharField(max_length=500,blank= False,default='',null=True )
    

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    def doExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False

    def validateEmail(self):
        email=self.email
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False


    def validatePhone(self):
            mob = self.mob
            from django.core.exceptions import ValidationError
            try:
                int(mob)
                return True
            except (ValueError, TypeError,ValidationError):
                return False

