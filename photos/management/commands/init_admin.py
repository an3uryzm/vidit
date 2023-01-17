"""
Django command to wait for the database to be available.
"""
import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Admin user creation check...')

        if User.objects.count() != 0:
            self.stdout.write('Admin already exists, no need to create new')
        else:
            admin = User.objects.create_superuser(  # type: ignore
                'admin', '', 'admin')

        self.stdout.write(self.style.SUCCESS(
            'Admin user creation check complete!'))
