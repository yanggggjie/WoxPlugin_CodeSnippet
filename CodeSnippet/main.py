# -*- coding: utf-8 -*-
from wox import Wox
import ast
import json
import win32clipboard as wc
import win32con


class Snippet(Wox):

    def load_data(self):
        """ 从json文件中加载并预处理数据 """
        with open("data.json", "r", encoding="utf8") as f:
            content = f.read()
            data = json.loads(content)
        # 处理数据
        titles_list = list(data.keys())
        values_list = list(data.values())
        # items是最终保留的数据项
        self.items = []
        for i in range(len(values_list)):
            # 取出每个value字典
            value_dict = values_list[i]
            # 加入title属性
            value_dict['title'] = titles_list[i]
            # 处理完成后append到items后面
            self.items.append(value_dict)

    def query(self, key_word):
        """ query查询函数,从wox launcher接受数据，进行处理后返回结果 """
        answers = []  # 进行匹配后的结果列表
        results = []  # 经过处理后，返回到wox launcher中进行显示的列表
        # 判断是否加载数据，没有的话那么要先加载数据
        if 'data' not in self.__dict__:
            self.load_data()
        # 进行模糊匹配（当key_word为prefix的字串时，我们认为完成匹配）
        for i in range(len(self.items)):
            item = self.items[i]
            if key_word in item['prefix']:
                answers.append(item)
        # 用answers (查询结果列表) 来生成results (wox launcher显示的列表)
        for answer in answers:
            results.append(
                {
                    # 显示标题
                    "Title": "{0:}：{1:}".format(answer['prefix'], answer['title']),
                    # 子标题
                    "SubTitle": "description：{0:}".format(answer['description']),
                    # 显示图标
                    "IcoPath": "Images/paste.png",
                    # 选中项目，按下enter后激活的函数
                    "JsonRPCAction": {
                        # 激活的函数名
                        'method': 'take_action',
                        # 需要传递的参数，注意：这里通过json传递，不能有换行符，传过去的是列表字符串
                        'parameters': ["{:}".format(answer['body'])],
                        # 激活后是否关闭wox launcher
                        'dontHideAfterAction': False
                    }
                })
        return results

    def setCopy(self, string):
        """ 写入粘贴板 """
        wc.OpenClipboard()
        wc.EmptyClipboard()
        wc.SetClipboardData(win32con.CF_UNICODETEXT, string)
        wc.CloseClipboard()

    def take_action(self, snippet_body):
        """  被选中项目激活的函数 """
        # 将字符串列表还原为列表
        snippet_body = ast.literal_eval(snippet_body)
        # 将列表还原成代码段落
        snippet_body = '\n'.join(snippet_body)
        # 写入粘贴板
        self.setCopy(snippet_body)
        return None


if __name__ == "__main__":
    Snippet()
