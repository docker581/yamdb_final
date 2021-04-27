from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.username = username
        user.save()
        return user

    def create_superuser(self, email, password, username=None):
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(email, password, username)
        user.is_superuser = True
        user.is_staff = True
        user.role = 'admin'
        user.save()
        return user
