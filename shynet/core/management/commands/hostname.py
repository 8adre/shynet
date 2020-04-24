import traceback
import uuid

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand, CommandError
from django.utils.crypto import get_random_string

from core.models import User


class Command(BaseCommand):
    help = "Configures the Shynet hostname"

    def add_arguments(self, parser):
        parser.add_argument(
            "hostname", type=str,
        )

    def handle(self, *args, **options):
        site = Site.objects.get(pk=settings.SITE_ID)
        site.domain = options.get("hostname")
        site.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully set the hostname to '{options.get('hostname')}'"
            )
        )
