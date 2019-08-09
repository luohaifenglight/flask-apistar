#! coding: utf-8
from simple.urls import simple_ns, urls as simple_urls


# Centralized Routing Control

blueprints = [
    ("/api/v1", "api"),
    ("/openapi/v1", "openapi"),
    ("/admin", "admin")
]

routes = {
    "api": [

        ("/simple", simple_ns, simple_urls)

    ],
    "openapi": [],
    "admin": []

}
