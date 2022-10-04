import binascii
import os

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Avg
from model_utils.models import TimeStampedModel
from rest_framework_jwt.settings import api_settings

ACCOUNT_TYPES = (
    ("Admin", "Admin"),
    ("Worker", "Worker")
)

class UserManager(BaseUserManager):
    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        # email = self.normalize_email(email)
        is_active = extra_fields.pop("is_active", True)
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        is_staff = extra_fields.pop("is_staff", False)
        return self._create_user(username, password, is_staff, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, True, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True) # db_index=True
    email = models.EmailField(
        "email address", max_length=255, unique=False, blank=True, null=True
    )
    account_type = models.CharField(max_length=32, choices=ACCOUNT_TYPES)
    
    first_name = models.CharField(max_length=32, default="", blank=True, null=True)
    last_name = models.CharField(max_length=32, default="", blank=True, null=True)
    age = models.CharField(max_length=32, blank=True, null=True)
    location = models.CharField(max_length=32, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True) #


    is_staff = models.BooleanField("staff status", default=False)
    is_active = models.BooleanField("active", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username" # Making username the required field
    REQUIRED_FIELDS = []

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)

        return token

def generate_password_reset_code():
    return binascii.hexlify(os.urandom(20)).decode("utf-8")


COUNTRIES = (
    ("UAE", "UAE"),
    ("Saudi Arabia", "Saudi Arabia"),
    ("Bahrain", "Bahrain"),
    ("Oman", "Oman"),
    ("Somalia", "Somalia"),
    ("Qatar", "Qatar"),
    ("Iraq", "Iraq"),
    ("Afganistan", "Afganistan"),
    ("Mali", "Mali"),
    ("Booking", "Booking"),
)

class RecruitmentAgency(models.Model):
    registered_name = models.CharField(max_length=52, unique=True)
    contact = models.CharField(max_length=52, unique=True)
    email = models.CharField(max_length=52, blank=True, null=True)
    premises = models.CharField(max_length=52, blank=True, null=True)
    registration_number = models.CharField(max_length=52, blank=True, null=True)
    no_workers_affiliated = models.CharField(max_length=52, blank=True, null=True)
    countries = models.CharField(max_length=52, blank=True, null=True, help_text="Please add a list of the countries the agency sends people to.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Recuitment Agency"
        verbose_name_plural = "Recuitment Agencies"

    def __str__(self):
        return '{}, {}'.format(self.registered_name)

class Worker(models.Model):
    full_name = models.CharField(max_length=52)
    contact = models.CharField(max_length=52, unique=True)
    email = models.CharField(max_length=52, blank=True, null=True)
    nin = models.CharField(max_length=100, blank=True, null=True)
    origin_location = models.CharField(max_length=52, blank=True, null=True)
    registration_number = models.CharField(max_length=52, blank=True, null=True)

    country_of_destination = models.CharField(max_length=52, choices=COUNTRIES)
    agency = models.ForeignKey(RecruitmentAgency, on_delete=models.DO_NOTHING, related_name="agency")
    countries_been_to = models.CharField(max_length=52, blank=True, null=True, help_text="Please add a list of the countries the agency sends people to.")
    contract_start_date = models.DateField(auto_now_add=True, blank=True, null=True)
    contract_end_date = models.DateField(auto_now_add=True, blank=True, null=True)

    employment_company = models.CharField(max_length=100, blank=True, null=True)
    work_place_location = models.CharField(max_length=100, blank=True, null=True)
    employer_name = models.CharField(max_length=100, blank=True, null=True)
    employer_contact = models.CharField(max_length=100, blank=True, null=True)
    employer_email = models.CharField(max_length=100, blank=True, null=True)
    employer_work_place = models.CharField(max_length=100, blank=True, null=True)
    employer_company = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"

    def __str__(self):
        return '{}, {}'.format(self.full_name)





