from django import template
from django.utils.http import urlencode

register = template.Library()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    """
    Generates a URL-encoded query string by combining the parameters from the context
    dictionary and the **kwargs dictionary.

    Args:
        context (dict): The context dictionary containing the request object.
        **kwargs (dict): Additional key-value pairs to be included in the query string.

    Returns:
        str: A URL-encoded query string.

    Raises:
        None
    """
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)