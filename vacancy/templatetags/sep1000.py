"""Format prices - separate thousands"""
from typing import Union

from django import template

register = template.Library()


@register.filter
def sep1000(number: int):
    return f"{number:,}".replace(',', ' ')
