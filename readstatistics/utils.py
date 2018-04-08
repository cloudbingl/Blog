import datetime
from django.contrib.contenttypes.models import ContentType
from django.db.models.fields import exceptions
from django.utils import timezone
from django.db.models import Sum
from django.db.models import Q

from .models import ReadNum
from .models import ReadDetail


class ReadNumMethod(object):
    def __init__(self):
        self.flag = ""

    def get_read_num(self):
        """获取文章阅读数量"""
        ct = ContentType.objects.get_for_model(self)
        try:
            num = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return num.read_num
        except exceptions.ObjectDoesNotExist:
            return 0

    def _check_read_flag(self, request):
        """
        检查文章是否已被阅读
        如果已读，返回 False
        如果未读，将对于文章阅读量+1，并返回 True
        """
        ct = ContentType.objects.get_for_model(self)
        # 已阅读的Cookie标志
        self.flag = '{}_{}_read_status'.format(ct.model, self.pk)
        if not request.COOKIES.get(self.flag):
            # 如果查询不到Cookies中有已阅读的标志，再将阅读量 +1
            # .get_or_create() 使用说明
            # 如果存在 -> obj,False
            # 如果不存在 -> 根据条件创建obj -> obj,True
            obj, created = ReadNum.objects.get_or_create(content_type=ct,
                                                         object_id=self.pk)
            obj.read_num += 1
            obj.save()
            obj_detail, created = ReadDetail.objects.get_or_create(
                content_type=ct,
                object_id=self.pk,
                date=timezone.now().date())
            obj_detail.date_read_num += 1
            obj_detail.save()
            return True
        return False

    def _set_read_flag(self, response):
        """设置Cookie标记"""
        response.set_cookie(self.flag, 'have_read')

    def check_or_set_read_flag(self, request, response):
        """
        用来检查用户是否已经对文章进行了阅读，
        如果已阅读，直接返回
        如果未阅读，在数据库中对文章的阅读量+1，并设置cookies标记
        :param request: 用户的请求对象
        :param response: 需要返回的响应对象
        :return:
        """
        if self._check_read_flag(request):
            self._set_read_flag(response)
        else:
            return


class ReadStatisticsMethod(object):
    today = timezone.now()

    @classmethod
    def get_seven_days_hot(cls):
        """获取7天内的热门文章数据"""
        seven_days = cls.today - datetime.timedelta(days=7)
        return cls._fetch_date(seven_days)

    @classmethod
    def get_thirty_days_hot(cls):
        """
        获取30天内的热门文章数据
        """
        thirty_days = cls.today - datetime.timedelta(days=7)
        return cls._fetch_date(thirty_days)

    @classmethod
    def _fetch_date(cls, some_days):
        """
        根据日期，获取对应天数的文章数据，并按阅读数量倒序排列。
        """
        hot_data = cls.objects.filter(
            Q(read_detail__date__lt=cls.today) & \
            Q(read_detail__date__gte=some_days)) \
            .annotate(read_num_sum=Sum('read_detail__date_read_num')) \
            .order_by('-read_num_sum')
        return hot_data


class ReadMethod(ReadNumMethod, ReadStatisticsMethod):
    pass