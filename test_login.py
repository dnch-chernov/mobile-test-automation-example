class TestLogin:
    def test_login(self, default_user, login_page, dashboard_page):
        assert login_page.is_correct()
        assert login_page.button_submit.is_inactive()
        login_page.field_email.type(default_user.email)
        login_page.field_password.type(default_user.password)
        assert login_page.button_submit.is_active()
        login_page.button_submit.click()
        assert dashboard_page.is_correct()
