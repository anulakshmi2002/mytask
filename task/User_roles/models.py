from django.db import models

# Create your models here.
class User(models.Model):
    User_id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=50)
    Place = models.CharField(max_length=60)
    email=models.EmailField(max_length=50)

    def __str___(self):
        return self.Username



class Role(models.Model):
    Role_id = models.AutoField(primary_key=True)
    Password = models.CharField(max_length=50 , unique=True)
    Phone_Number = models.CharField(max_length=50 ,unique=True)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)


class UserRole(models.Model):
    ACTIVE = 'Active'
    DISABLE = 'Disable'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (DISABLE, 'Disable'),
    ]

    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)


class UserLog(models.Model):
    LOGIN = 'Login'
    LOGOUT = 'Logout'
    ROLE_CHANGE = 'Role Change'
    ACTION_CHOICES = [
        (LOGIN, 'Login'),
        (LOGOUT, 'Logout'),
        (ROLE_CHANGE, 'Role Change'),
    ]

    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    role_changed_from = models.ForeignKey('Role', related_name='role_changed_from', on_delete=models.SET_NULL, null=True, blank=True)
    role_changed_to = models.ForeignKey('Role', related_name='role_changed_to', on_delete=models.SET_NULL, null=True, blank=True)


