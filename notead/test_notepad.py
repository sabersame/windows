import pytest
from case.case_notepad import Case_Notepad
from public.Data_Unit import Data_Base


class Test_Notepad:
    data_list = Data_Base("notepad").result

    def setup_class(self):
        self.d = Case_Notepad()
        self.d.start_log()

    def teardown_class(self):
        self.d.end_log()

    def test_error_login(self, edit_text=data_list['edit_text'], case_name="notepad_stream"):
        self.d.edittext_input_click(case_name)
        self.d.edittext_input_input(case_name, edit_text[0])
        self.d.edittext_input_input(case_name, edit_text[1])
        self.d.restore_button_click(case_name)
        self.d.close_button_click(case_name)
        self.d.notsave_button_click(case_name)

