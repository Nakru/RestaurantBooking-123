from unittest import TestCase


class TestSmsSenderSender(TestCase):
    def send(self, schedule):
        print("테스트용 SMSSender 에서 send 메소드 실행")
        self.__send_method_is_called = True

    def is_send_method_is_called(self):
        return self.__send_method_is_called

class TestMailSender(TestCase):
    def __init__(self):
        self.count_send_mail_is_called = 0
    def send_mail(self, schedule):
        self.count_send_mail_is_called += 1

    def get_count_send_mail_is_called(self):
        return self.count_send_mail_is_called
