from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone


class AccountUserManager(UserManager):
    def _create_user(self, first_name, username, email, password, is_staff, is_superuser, image, **extra_fields):
        """
       Creates and saves a User with the given username, email and password.
       """
        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, image=image,
                          date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractUser):
    # now that we've abstracted this class we can add any
    # number of custom attribute to our user class

    # in later units we'll be adding things like payment details!
    stripe_id = models.CharField(max_length=40, default='')
    subscription_end = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    objects = AccountUserManager()

    def is_subscribed(self, house):
        try:
            purchase = self.purchases.get(house__pk=house.pk)
        except Exception:
            return False

        if purchase.subscription_end > timezone.now():
            return False

        return True
