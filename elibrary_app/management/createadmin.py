import os

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        username = os.environ.get(
            "ADMIN_USERNAME"
        )

        email = os.environ.get(
            "ADMIN_EMAIL"
        )

        password = os.environ.get(
            "ADMIN_PASSWORD"
        )


        if not User.objects.filter(
            username=username
        ).exists():

            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )

            self.stdout.write(
                "Admin created"
            )

        else:

            self.stdout.write(
                "Admin already exists"
            )