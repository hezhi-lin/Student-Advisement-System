# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('myproject.myapp.views',
    url(r'^home/$', 'home', name='home'),
    url(r'^uploadFile/$', 'uploadFile', name='uploadFile'),
    url(r'^cloneProgram/$', 'cloneProgram', name='cloneProgram'),
    url(r'^selectProgram/$', 'selectProgram', name='selectProgram'),
    url(r'^selectSection/$', 'selectSection', name='selectSection'),
    url(r'^selectEmphasis/$', 'selectEmphasis', name='selectEmphasis'),
    url(r'^viewTranscript/$', 'viewTranscript', name='viewTranscript'),
    url(r'^viewGTranscript/$', 'viewGTranscript', name='viewGTranscript'),

)
