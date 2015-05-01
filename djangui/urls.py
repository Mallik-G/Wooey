from django.conf.urls import include, url
from django.conf import settings

# from djangui.admin import
from djangui.views import celery_status, CeleryTaskView, celery_task_command, DjanguiScriptJSON, DjanguiHomeView, DjanguiRegister


urlpatterns = [
    url(r'^celery/command$', celery_task_command, name='celery_task_command'),
    url(r'^celery/status$', celery_status, name='celery_results'),
    url(r'^celery/(?P<job_id>[a-zA-Z0-9\-]+)/$', CeleryTaskView.as_view(), name='celery_results_info'),
    # url(r'^admin/', include(djangui_admin.urls)),
    url(r'^djscript/(?P<script_group>[a-zA-Z0-9\-\_]+)/(?P<script_name>[a-zA-Z0-9\-\_]+)/(?P<task_id>[a-zA-Z0-9\-]+)$',
        DjanguiScriptJSON.as_view(), name='djangui_script_clone'),
    url(r'^djscript/(?P<script_group>[a-zA-Z0-9\-\_]+)/(?P<script_name>[a-zA-Z0-9\-\_]+)/$', DjanguiScriptJSON.as_view(), name='djangui_script'),
    url(r'^$', DjanguiHomeView.as_view(), name='djangui_home'),
    url(r'^$', DjanguiHomeView.as_view(), name='djangui_task_launcher'),
    url('^', include(getattr(settings, 'DJANGUI_AUTH_URLS', 'django.contrib.auth.urls'))),
    url('^register/$', getattr(settings, 'DJANGUI_REGISTER_URL', DjanguiRegister.as_view()), name='djangui_register'),
]