from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email               = models.EmailField(unique=True)
    nom                 = models.CharField(max_length=150)
    prenom              = models.CharField(max_length=150)
    dateDeNaissance     = models.DateField()
    dateCreationCompte  = models.DateField(auto_now_add=True)
    private             = models.BooleanField(default=True)
    profilePic          = models.FileField(upload_to='profile_pics/', blank=True, null=True)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom', 'dateDeNaissance']

    def __str__(self):
        return f"{self.nom} {self.prenom} né le {self.dateDeNaissance}"

    class Meta:
        db_table = 'user_user'

class Follow(models.Model):
    dateFollow = models.DateField(default=timezone.now)
    followerID = models.IntegerField()
    followedID = models.IntegerField()

    class Meta:
        db_table = 'user_follow'

class UserFollow(models.Model):
    follower = models.ForeignKey(get_user_model(), related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(get_user_model(), related_name='followers', on_delete=models.CASCADE)
    date_followed = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')