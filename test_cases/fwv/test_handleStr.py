from time import sleep

from fwv.handleStr import handleString

class TestHandleStr:

    def test_get_words(self):
        sleep(5)
        str = 'like a apple'
        list = ['l', 'i', 'e', 'p', 'p', 'l', 'e']
        assert list.sort() == handleString.get_words(str)

    def test_get_words_incorrect(self):
        """
        异常用例，原函数未指明大小写
        :return:
        """
        sleep(3)
        str = 'like A Apple'
        list = ['l', 'i', 'e', 'p', 'p', 'l', 'e']
        assert list.sort() == handleString.get_words(str)
