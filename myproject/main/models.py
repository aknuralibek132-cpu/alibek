from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.CharField(max_length=200, blank=True, verbose_name="Адрес")

    # добавляем аватар
    avatar = models.ImageField(
        upload_to='avatars/',       # папка внутри MEDIA_ROOT
        blank=True,                 # не обязательно заполнять
        null=True,                  # можно оставить пустым в базе
        verbose_name="Аватар"
    )

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")

    def __str__(self):
        return f"Заказ №{self.id} от {self.client.name}"


class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Остаток на складе")

    def __str__(self):
        return f"{self.product.name} — {self.quantity} шт."

class SpecialOffer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Скидка (%)",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        verbose_name = "Спец предложение"
        verbose_name_plural = "Спец предложения"

    def clean(self):
        if self.start_date and self.end_date and self.end_date < self.start_date:
            raise ValidationError("Дата окончания должна быть позже или равна дате начала.")

    def __str__(self):
        return f"{self.product.name} — {self.discount}% ({self.start_date} — {self.end_date})"
    

class Promotion(models.Model):

    DISCOUNT_TYPE_CHOICES = [
        ('percent', 'Процентная скидка'),
        ('fixed', 'Фиксированная сумма'),
    ]

    promotion_name = models.CharField(max_length=255, verbose_name="Название продвижения")

    discount_type = models.CharField(
        max_length=20,
        choices=DISCOUNT_TYPE_CHOICES,
        verbose_name="Тип скидки"
    )

    discount_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Размер скидки",
        help_text="Процент или фиксированная сумма"
    )

    applicable_products = models.ManyToManyField(
        Product,
        related_name="promotions",
        blank=True,
        verbose_name="Применимые продукты"
    )

    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")

    minimum_order_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Минимальная сумма заказа"
    )

    priority = models.IntegerField(
        default=0,
        verbose_name="Приоритет",
        help_text="Большее число означает более высокий приоритет"
    )

    class Meta:
        verbose_name = "Продвижение"
        verbose_name_plural = "Продвижения"
        ordering = ['-priority', 'start_date']

    def clean(self):
        if self.end_date and self.start_date and self.end_date < self.start_date:
            raise ValidationError("Дата окончания должна быть позже даты начала.")

    def __str__(self):
        return f"{self.promotion_name} (ID: {self.id})"

class LoyaltyMembership(models.Model):

    MEMBERSHIP_LEVELS = [
        ('basic', 'Basic'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
    ]

    client = models.OneToOneField(
        Client,
        on_delete=models.CASCADE,
        related_name="loyalty",
        verbose_name="Клиент",
    )

    membership_status = models.CharField(
        max_length=20,
        choices=MEMBERSHIP_LEVELS,
        default='basic',
        verbose_name="Статус участника"
    )

    loyalty_points = models.PositiveIntegerField(
        default=0,
        verbose_name="Баллы лояльности"
    )

    total_spending = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Общая сумма покупок"
    )

    registration_date = models.DateField(
        default=timezone.now,
        verbose_name="Дата регистрации"
    )

    def __str__(self):
        return f"{self.client.name} ({self.membership_status}) — {self.loyalty_points} pts"


# --------------------------------------------
# Лог перерасчёта баллов
# --------------------------------------------
class LoyaltyRecalculationLog(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    recalculated_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата перерасчёта")
    old_points = models.IntegerField(verbose_name="Старые баллы")
    new_points = models.IntegerField(verbose_name="Новые баллы")
    details = models.TextField(verbose_name="Подробности начисления")

    def __str__(self):
        return f"Recalc for {self.client.name} — {self.recalculated_at}"


# --------------------------------------------
# Вознаграждения (погашения)
# --------------------------------------------
class LoyaltyReward(models.Model):

    REWARD_TYPES = [
        ('discount_5', 'Скидка 5€'),
        ('discount_10_percent', 'Скидка 10%'),
        ('upgrade_level', 'Повышение уровня'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    reward_type = models.CharField(max_length=30, choices=REWARD_TYPES, verbose_name="Тип награды")
    redeemed_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата погашения")

    # Если создаётся скидка — ссылка на Promotion
    created_promotion = models.ForeignKey(
        Promotion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Созданное продвижение"
    )

    notes = models.TextField(blank=True, verbose_name="Примечание")

    def __str__(self):
        return f"{self.client.name} — {self.get_reward_type_display()} ({self.redeemed_at})"

