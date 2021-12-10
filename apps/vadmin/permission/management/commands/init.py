import logging
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connection

from apps.vadmin.scripts import getSql

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    python manage.py init
    """

    def customSql(self, sql_list, model_name, table_name, is_yes):
        """
        sql
        :param sql_list:
        :param table_name:
        :return:
        """
        with connection.cursor() as cursor:
            num = 0
            for ele in table_name.split(','):
                cursor.execute("select count(*) from {}".format(ele))
                result = cursor.fetchone()
                num += result[0]
            if num > 0:
                while True:
                    if is_yes is None:
                        inp = input(f'[{model_name}]Mô hình đã được khởi tạo và sẽ tiếp tục bị xóa[{table_name}]Tất cả dữ liệu trong bảng, có tiếp tục khởi chạy hay không？【 Y/N 】')
                    else:
                        inp = 'Y' if is_yes == True else 'N'
                    if inp.upper() == 'N':
                        return False
                    elif inp.upper() == 'Y':
                        logger.info(f'Làm trống[{table_name}]dữ liệu trung bình...')
                        cursor.execute("SET foreign_key_checks = 0")
                        for ele in table_name.split(','):
                            cursor.execute("truncate table {};".format(ele))
                        cursor.execute("SET foreign_key_checks = 1")
                        connection.commit()
                        logger.info(f'Trống[{table_name}]dữ liệu trung bình{result[0]}dải')
                        break

            for sql in sql_list:
                try:
                    cursor.execute(sql)
                except Exception as e:
                    print(e)
            connection.commit()
            return True

    def init(self, sql_filename, model_name, table_name, is_yes):
        """
        :param sql_filename: sql
        :param model_name:
        :param table_name:
        :return:
        """
        logger.info(f'Khởi tạo[{model_name}]ở giữa...')
        if self.customSql(getSql(sql_filename), model_name, table_name, is_yes):
            logger.info(f'[{model_name}]tải xong！')
        else:
            logger.info(f'Đã hủy[{table_name}]sự khởi tạo')

    def add_arguments(self, parser):
        parser.add_argument('init_name', nargs='*', type=str, )
        parser.add_argument('-y', nargs='*')
        parser.add_argument('-Y', nargs='*')
        parser.add_argument('-n', nargs='*')
        parser.add_argument('-N', nargs='*')

    def handle(self, *args, **options):
        user_name = "_".join(settings.AUTH_USER_MODEL.lower().split("."))
        init_dict = {
            'system_dictdata': [os.path.join('system', 'system_dictdata.sql'), 'Quản lý từ điển', 'system_dictdata'],
            'system_dictdetails': [os.path.join('system', 'system_dictdetails.sql'), 'Chi tiết từ điển', 'system_dictdetails'],
            'system_configsettings': [os.path.join('system', 'system_configsettings.sql'), 'Cài đặt tham số',
                                      'system_configsettings'],
            'permission_post': [os.path.join('permission', 'permission_post.sql'), 'Quản lý công việc', 'permission_post'],
            'permission_dept': [os.path.join('permission', 'permission_dept.sql'), 'Quản lý bộ phận', 'permission_dept'],
            'permission_menu': [os.path.join('permission', 'permission_menu.sql'), 'Quản lý menu', 'permission_menu'],
            'permission_role': [os.path.join('permission', 'permission_role.sql'), 'Quản lý vai trò',
                                ','.join(['permission_role', 'permission_role_dept', 'permission_role_menu'])],
            'permission_userprofile': [os.path.join('permission', 'permission_userprofile.sql'), 'Quản lý người dùng', ','.join(
                [f'{user_name}_groups', f'{user_name}', f'{user_name}_role', f'{user_name}_post'])]
        }
        init_name = options.get('init_name')
        is_yes = None
        if isinstance(options.get('y'), list) or isinstance(options.get('Y'), list):
            is_yes = True
        if isinstance(options.get('n'), list) or isinstance(options.get('N'), list):
            is_yes = False
        if init_name:
            [self.init(*init_dict[ele], is_yes=is_yes) for ele in init_name if ele in init_dict]
        else:
            for ele in init_dict.values():
                self.init(*ele, is_yes=is_yes)
