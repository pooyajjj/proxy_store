# from django.contrib.auth.models import BaseUserManager




# class UserManager(BaseUserManager):

#     def create_user(self, phone_num, email, first_name, password):
#         if not phone_num:
#             raise ValueError('user must have phone number')

#         if not email:
#             raise ValueError('user must have email')

#         if not first_name:
#             raise ValueError('user must have full name')

#         user = self.model(phone_num=phone_num, email=self.normalize_email(email), first_name=first_name)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user


#     def create_superuser(self, username, password, email, first_name):
#         user = self.create_user(username, password,  email, first_name)
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
        