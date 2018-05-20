from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from ..models import Favour, FavourDetail

register = template.Library()


@register.simple_tag()
def get_favour_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    favour, created = Favour.objects.get_or_create(content_type=content_type,
                                                   object_id=obj.pk)
    return favour.favour_num


# @register.simple_tag(takes_context=True)
# def get_favour_status(context, obj):  -> user=context['user']

@register.simple_tag()
def get_favour_status(obj, user):
    content_type = ContentType.objects.get_for_model(obj)

    favour_detail = FavourDetail.objects.filter(
        content_type=content_type,
        object_id=obj.pk,
        user=user
    )
    if favour_detail.exists():
        return 'active'
    else:
        return None