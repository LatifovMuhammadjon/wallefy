from django.db import models
from django.utils.translation import gettext_lazy as _


CURRENCY_CHOICES = (
    ('UZS', 'UZS'),
    ('RUB', 'RUB'),
    ('USD', 'USD'),
)


class BaseModel(models.Model):
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(_('category name'), max_length=63)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('category')


class InCome(BaseModel):
    quantity = models.DecimalField(_("quantity"), max_digits=20,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    currency = models.CharField(
        _('currency'),
        max_length=3,
        choices=CURRENCY_CHOICES
    )

    def __str__(self):
        return f'{self.quantity} {self.currency}'

    class Meta:
        verbose_name = _('income')
        verbose_name_plural = _('income')


class OutCome(BaseModel):
    quantity = models.DecimalField(_("quantity"), max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    currency = models.CharField(
        _('currency'),
        max_length=3,
        choices=CURRENCY_CHOICES
    )

    def __str__(self):
        return f'{self.quantity} {self.currency}'

    class Meta:
        verbose_name = _('outcome')
        verbose_name_plural = _('outcome')
