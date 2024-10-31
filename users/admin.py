from django.contrib import admin

from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not(obj.password == request.user.password):
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
