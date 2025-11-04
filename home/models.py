# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    channel_name = models.CharField(max_length=255, null=True, blank=True)
    channel_title = models.CharField(max_length=255, null=True, blank=True)
    oracle_address = models.CharField(max_length=255, null=True, blank=True)
    oracle_sid = models.CharField(max_length=255, null=True, blank=True)
    oracle_port = models.IntegerField(null=True, blank=True)
    oracle_version = models.CharField(max_length=255, null=True, blank=True)
    oracle_location = models.CharField(max_length=255, null=True, blank=True)
    kafka_address = models.CharField(max_length=255, null=True, blank=True)
    kafka_default_topic = models.CharField(max_length=255, null=True, blank=True)
    kafka_location = models.CharField(max_length=255, null=True, blank=True)
    kafka_topic_template = models.CharField(max_length=255, null=True, blank=True)
    connector_guid = models.CharField(max_length=255, null=True, blank=True)
    oracle_table_file = models.CharField(max_length=255, null=True, blank=True)
    pii_exception_file = models.CharField(max_length=255, null=True, blank=True)
    snowflake_db_name = models.CharField(max_length=255, null=True, blank=True)
    wms_type = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__

#__MODELS__END
