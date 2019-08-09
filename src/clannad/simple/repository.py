#! coding: utf-8
from simple.models import SimpleCollection


def test_result():
    result = SimpleCollection.objects.all()
    return result
