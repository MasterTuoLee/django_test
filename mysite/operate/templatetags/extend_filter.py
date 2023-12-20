from django.template import Library
from ..models import Collect
register = Library()


@register.filter
def test_filter(value, info):
    return "hello"+value+info


# 使用方式 1. 在模板中使用{% load extend_filter %}
# 2. {{ news|is_collect:request.user }}
@register.filter
def is_collect(news, user):
    collect = Collect.objects.filter(user=user, news=news).first()
    if collect:
        return True
    return False
