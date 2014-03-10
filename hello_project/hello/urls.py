from django.conf.urls import patterns, url

urlpatterns = patterns('hello.views',
    url('', 'hi'),
)
