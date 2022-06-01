import django
from django.conf.urls import path
from django_useragent.tests import views


if django.VERSION >= (1, 8):
    urlpatterns = [
        path("user-agents/", views.test, name="user_agent_test"),
        path("filters/", views.test_filters, name="user_agent_test_filters"),
    ]
else:
    from django.conf.urls import patterns

    urlpatterns = patterns(
        "django_useragent.tests.views",
        path("user-agents/", "test", name="user_agent_test"),
        path("filters/", "test_filters", name="user_agent_test_filters"),
    )
