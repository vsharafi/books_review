from django import template


register = template.Library()

#
# @register.filter(name='to_low')
# def to_lowercase(value):
#     return value.capitalize()
