import logging
import os
import shutil

from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)
from root.settings import BASE_DIR


class Command(BaseCommand):
    """
    App:
    python manage.py createapp app
    python manage.py createapp app01 app02 ...
    python manage.py createapp /app01 ...    # app
    """

    def add_arguments(self, parser):
        parser.add_argument('app_name', nargs='*', type=str, )

    def handle(self, *args, **options):
        app_name = options.get('app_name')
        for name in app_name:
            names = name.split('/')
            dnames = ".".join(names)
            app_path = os.path.join(BASE_DIR, "apps", *names)
            if os.path.exists(app_path):
                print(f"Tạo không thành công，App {name} tồn tại！")
                break
            source_path = os.path.join(BASE_DIR, "apps", "vadmin", "template")
            target_path = app_path
            if not os.path.exists(target_path):
                os.makedirs(target_path)
            if os.path.exists(source_path):
                shutil.rmtree(target_path)
            shutil.copytree(source_path, target_path)
            content = f"""from django.apps import AppConfig


class {name[-1].capitalize()}Config(AppConfig):
    name = 'apps.{dnames}'
    verbose_name = "{names[-1]}App"
"""
            with open(os.path.join(app_path, "apps.py"), 'w', encoding='UTF-8') as f:
                f.write(content)
                f.close()
            injection(os.path.join(BASE_DIR, "application", "settings.py"), f"    'apps.{dnames}',\n", "INSTALLED_APPS",
                      "]")

            injection(os.path.join(BASE_DIR, "application", "urls.py"),
                      f"    re_path(r'^{name}/', include('apps.{dnames}.urls')),\n", "urlpatterns = [",
                      "]")

            print(f"创建 {name} App成功")


def injection(file_path, insert_content, startswith, endswith):
    with open(file_path, "r+", encoding="utf-8") as f:
        data = f.readlines()
        with open(file_path, 'w', encoding='UTF-8') as f1:
            is_INSTALLED_APPS = False
            is_insert = False
            for content in data:
                if not is_insert and content.startswith(startswith):
                    is_INSTALLED_APPS = True
                if not is_insert and content.startswith(endswith) and is_INSTALLED_APPS:
                    content = insert_content + content
                    is_insert = True
                f1.writelines(content)
