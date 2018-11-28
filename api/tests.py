from rest_framework.test import APITestCase


class BaseTestCase(APITestCase):

    # 导入测试数据到测试数据库
    fixtures = [
        "data.json",
    ]

    def setUp(self):
        pass
