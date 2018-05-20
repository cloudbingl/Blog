from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

from .models import Favour, FavourDetail


def favour_changed(request):
    # 没有登录不能点赞
    if not request.user.is_authenticated:
        return JsonResponse({'code': 401, 'text': '登陆后可以点赞'})

    user = request.user
    ct = request.GET.get('content_type', '')
    obj_id = request.GET.get('object_id', '')
    try:
        # 通过model名称查询ContentType对象，然后获取模型类，查询对象是否存在
        content_type = ContentType.objects.get(model=ct)
        model_class = content_type.model_class()
        obj = model_class.objects.get(pk=obj_id)
    except ObjectDoesNotExist:
        # 不存在返回错误信息
        return JsonResponse({'code': 404, 'text': '点赞的对象不存在'})

    # 创建 或 获取该点赞详情
    favour_detail, created = FavourDetail.objects.get_or_create(
        user=user,
        content_type=content_type,
        object_id=obj_id
    )
    if created:
        # 点赞
        favour, created = Favour.objects.get_or_create(
            content_type=content_type,
            object_id=obj_id
        )
        favour.favour_num += 1
        favour.save()
        return JsonResponse({'code': 201, 'text': "点赞成功"})
        # return JsonResponse({'code': 403, 'text': '不可重复点赞'})
    else:
        # 取消点赞
        favour_detail = FavourDetail.objects.filter(
            user=user,
            content_type=content_type,
            object_id=obj_id
        )
        if not favour_detail.exists():
            # 查询结果不存在
            return JsonResponse({'code': 404, 'text': '取消点赞的对象不存在'})
        favour_detail.delete()
        favour = Favour.objects.get(content_type=content_type,
                                    object_id=obj_id)
        favour.favour_num -= 1
        favour.save()
        return JsonResponse({'code': 200, 'text': '取消点赞'})

