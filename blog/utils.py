import math
import re


from django.utils.html import strip_tags

from django_editorjs_fields.templatetags import editorjs


def count_words(string):
    word_string = strip_tags(string)
    matching_words = re.findall(r'\w+', word_string)
    count = len(matching_words)
    return count


def read_time(string):
    string = editorjs.editorjs(string)
    count = count_words(string)
    time_per_min = math.ceil(count/200.0)
    return int(time_per_min)