import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    help = "This command creates superuser"

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            user.avatar.delete(save=True)
        self.stdout.write(self.style.SUCCESS(f"Done!"))
