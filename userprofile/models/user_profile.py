import logging

from django.db import models

from utils.base_models import BaseUserModel

logger = logging.getLogger(__name__.split('.')[0])


class UserProfile(BaseUserModel):
    ADMIN = 'admin'
    VIP = 'vip'
    NORMAL = 'normal'

    MALE = 'male'
    FEMALE = 'female'

    LEVEL0 = '0'
    LEVEL1 = '1'
    LEVEL2 = '2'
    LEVEL3 = '3'
    LEVEL4 = '4'
    LEVEL5 = '5'

    USER_TYPES = (
        (ADMIN, 'Admin'),
        (VIP, 'Vip'),
        (NORMAL, 'Normal')
    )

    LEVEL = (
        (LEVEL0, '0'),
        (LEVEL1, '1'),
        (LEVEL2, '2'),
        (LEVEL3, '3'),
        (LEVEL4, '4'),
        (LEVEL5, '5'),
    )

    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    email = models.CharField(max_length=40, null=False, blank=False)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, default=MALE)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default=NORMAL)
    level = models.CharField(max_length=20, choices=LEVEL, default=LEVEL1)
    coin = models.IntegerField(default=0)
    card_story = models.IntegerField(default=1)
    avatar = models.ImageField(upload_to='userprofile/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return "%s" % self.full_name




