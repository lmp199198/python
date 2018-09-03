# -*- coding:utf-8 -*-
from common.base import Base

class NewBug(Base):
    '''提交BUG页面'''
    test_tab_loc = ("xpath", ".//*[@id='mainmenu']/ul/li[4]/a")  # 测试tab
    bug_loc = ("link text", "Bug")  # Bug按钮
    add_bug_loc = ("xpath", ".//*[@id='createActionMenu']/a")  # 点提BUG
    title_loc = ("id", "title")                           # 标题
    body_loc = ("class name", "article-content")        # 正文
    save_loc = ("id", "submit")    # 保存
    truck_loc = ("class name", "chosen-choices")
    add_truck_loc = ("css selector", ".active-result.highlighted")
    title = ("xpath", ".//*[@id='bugList']/tbody/tr[1]/td[4]")  # 提交成功后
    truck_top_loc = ("xpath", ".//*[@id='openedBuildLabel']")  # trunk弹出框上

    def click_test_tab(self):
        '''点Tab页切换：测试'''
        self.click(self.test_tab_loc)

    def click_bug(self):
        '''点加号'''
        self.click(self.bug_loc)

    def click_add_bug(self):
        '''点添加BUG'''
        self.click(self.add_bug_loc)

    def input_title(self, text):
        '''输入bug标题'''
        self.sendKeys(self.title_loc, text)

    def input_bug_detail(self, text):
        '''富文本里面输入内容'''
        self.driver.switch_to_frame(1)
        self.sendKeys(self.body_loc, text)
        self.driver.switch_to_default_content()

    def add_truk(self):
        '''影响版本'''
        self.click(self.truck_loc)
        self.click(self.add_truck_loc)

    def click_save(self):
        '''点保存按钮'''
        self.click(self.save_loc)

    def get_bug_title(self):
        '''获取返回结果'''
        # 考虑2种，成功返回什么，失败什么
        try:
            t = self.findElement(self.title).text
            return t
        except:
            return ""

    def get_truck_text(self):
        '''truck为空的时候弹出内容'''
        try:
            t = self.findElement(self.truck_top_loc).text
            return t
        except:
            return ""

    def is_truck_text_in(self, text):
        return self.is_text_in_element(self.truck_top_loc,text)
