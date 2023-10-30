from django.db import models
from user_phone_auth.lib import message
import json
import random
import datetime
from django.utils import timezone
from model_utils.models import TimeStampedModel


class PhoneAuth(TimeStampedModel):
    phone_number = models.CharField(
        verbose_name="휴대폰 번호", primary_key=True, max_length=11
    )
    auth_number = models.IntegerField(verbose_name="인증 번호")

    # class Meta(TimeStampedModel.Meta):
    #     db_table = "auth"

    def save(self, *args, **kwargs):
        self.auth_number = random.randint(100000, 999999)
        super().save(*args, **kwargs)
        # self.send_sms()
        print(self.auth_number)

    def send_sms(self):
        data = {
            "message": {
                "to": self.phone_number,
                "from": "01045665227",
                "text": "인증번호 [{}]를 입력해주세요.".format(self.auth_number),
            },
        }

        res = message.send_one(data)
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    @classmethod
    def check_auth_number(cls, p_num, c_num):
        time_limit = timezone.now() - datetime.timedelta(minutes=5)
        result = cls.objects.filter(
            phone_number=p_num, auth_number=c_num, modified__gte=time_limit
        )
        if result:
            return True
        return False
