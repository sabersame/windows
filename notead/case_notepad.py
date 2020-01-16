from common.Base_Unit import Base_Base


class Case_Notepad(Base_Base):
    """
    闻道作业测评测试的流程动作
    """
    def __init__(self):
        super().__init__()

    def edittext_input_input(self, case_name, text):
        self.input(case_name, "Edit", "ClassName", "Edit", "1", text)
        # 如果想光标快速移动到当前行的最前面/最后面, 可以传入{Home}/{End}
        # 换行的话可以传入{Enter}

    def edittext_input_click(self, case_name):
        self.click(case_name, "Edit", "ClassName", "Edit", "1")

    def restore_button_click(self, case_name):
        self.click(case_name, "Button", "Name", "还原", "2")

    def close_button_click(self, case_name):
        self.click(case_name, "Button", "Name", "关闭", "2")

    def notsave_button_click(self, case_name):
        self.click(case_name, "Button", "Name", "不保存(N)", "3")
        # 当然也可以使用键盘输入模拟选择
        # self.input(case_name, "Button", "Name", "不保存(N)", "3", {Alt}n)

    def start_log(self):
        self.log(self.Set.history_log, "info", "正在执行笔记本脚本......")

    def end_log(self):
        self.log(self.Set.history_log, "info", "笔记本脚本执行完毕.")




