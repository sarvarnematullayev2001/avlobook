# from django.db import models
#
# from core.base_model import BaseModel
#
#
# class SocialNetwork(BaseModel):
#     TELEGRAM = 'telegram'
#     FACEBOOK = 'facebook'
#     INSTAGRAM = 'instagram'
#     INTERNET = 'internet'
#     TYPE = (
#         (TELEGRAM, TELEGRAM),
#         (FACEBOOK, FACEBOOK),
#         (INSTAGRAM, INSTAGRAM),
#         (INTERNET, INTERNET),
#     )
#     user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='social_accounts')
#     name = models.CharField(max_length=25, choices=TYPE)
#     url = models.URLField()
