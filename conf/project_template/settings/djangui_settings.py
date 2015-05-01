from .django_settings import *

INSTALLED_APPS += (
    # 'corsheaders',
    'djangui',
)

# MIDDLEWARE_CLASSES = [[i] if i == 'django.middleware.common.CommonMiddleware' else ['corsheaders.middleware.CorsMiddleware',i] for i in MIDDLEWARE_CLASSES]
MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
MIDDLEWARE_CLASSES.append('{{ project_name }}.middleware.ProcessExceptionMiddleware')

PROJECT_NAME = "{{ project_name }}"
DJANGUI_CELERY_APP_NAME = 'djangui.celery'
DJANGUI_CELERY_TASKS = 'djangui.tasks'

DJANGUI_EXCLUDES = ('djangui_script_name', 'djangui_celery_id', 'djangui_celery_state',
                    'djangui_job_name', 'djangui_job_description', 'djangui_user', 'djangui_command')
