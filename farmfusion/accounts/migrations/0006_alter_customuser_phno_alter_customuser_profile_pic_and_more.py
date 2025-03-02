import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_alter_customuser_dob_alter_customuser_phno"),
    ]

    operations = [
        migrations.AlterField(

            model_name="customuser",
            name="phno",
            field=models.CharField(default="000000000", max_length=15),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="profile_pic",
            field=models.ImageField(blank=True, null=True, upload_to="pics"),
        ),
        migrations.CreateModel(
            name="Wallet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("wallet_amount", models.IntegerField(default=0)),
                ("free_amount", models.IntegerField(default=0)),
                ("is_locked", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wallet",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
