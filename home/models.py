from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager,PermissionsMixin


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, dni, password=None):
        if not email:
            raise ValueError("The email is required")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            dni=dni,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, dni, password):
        user = self.create_user(
            email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            dni=dni,
            password=password
        )
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser, PermissionsMixin):
    username = models.CharField('username', max_length=150, unique=True)
    email = models.EmailField('email address', unique=True, max_length = 255)
    biography = models.TextField()
    images = models.ImageField(upload_to="user/%Y/%m/%d", null=True, blank=True)
    dni = models.CharField(max_length=20, null=False, blank=False)
    admin = models.BooleanField(default=False)
    first_name = models.CharField('first_name', max_length=150, unique=False)
    last_name = models.CharField('last_name', max_length=150, unique=False)
    dni = models.CharField('last_name', max_length=150, unique=True)
    objects = UsuarioManager()
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self) -> str:
        return f"{self.first_name},{self.last_name}"

    @property
    def is_staff(self):
        return self.admin

    # telefono


class comments(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)


class rents(models.Model):
    rent_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=10, max_digits=15)
    location = models.CharField(max_length=300)
    published_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    reviews_nb = models.DecimalField(decimal_places=10, max_digits=20)
    reviews_avg = models.DecimalField(decimal_places=5, max_digits=20)
    comments = models.ForeignKey(comments, on_delete=models.CASCADE)
    bedrooms = models.DecimalField(decimal_places=4, max_digits=15)
    bathrooms = models.DecimalField(decimal_places=4, max_digits=15)
    total_guests_limit = models.DecimalField(decimal_places=4, max_digits=15)
    images = models.ImageField(upload_to="rent_images/%Y/%m/%d", null=True, blank=True)
