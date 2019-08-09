#! coding: utf-8

from simple.service import simple_ns, CurrentUserResource

urls = [
    ("/test", CurrentUserResource)
]
