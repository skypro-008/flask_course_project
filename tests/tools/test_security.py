from project.utils.security import compare_passwords, generate_password_hash


class TestSecurity:
    def test_generate_password_hash(self, app):
        password: str = "password"
        password_hash = generate_password_hash(password)
        assert isinstance(password_hash, str)
        assert password != password_hash

    def test_compare_passwords(self, app):
        password: str = "password"
        password_hash = generate_password_hash(password)
        assert compare_passwords(password_hash, password) is True
        assert compare_passwords(password_hash, "qwerty") is False
