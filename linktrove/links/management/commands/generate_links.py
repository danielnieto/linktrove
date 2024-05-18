from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from linktrove.links.factories import LinkFactory


class Command(BaseCommand):
    help = "Generate n number of Links and assign them to a specific user"

    def add_arguments(self, parser):
        parser.add_argument("user_id", type=int, help="User ID to assign links to")
        parser.add_argument("n", type=int, help="Number of links to generate")

    def handle(self, *args, **kwargs):
        user_id = kwargs["user_id"]
        n = kwargs["n"]

        # Get the user object
        User = get_user_model()
        user = User.objects.get(pk=user_id)

        # Generate n number of links and assign them to the user
        LinkFactory.create_batch(n, user=user)

        self.stdout.write(
            self.style.SUCCESS(
                f"{n} links created and assigned to User with ID: {user_id}"
            )
        )
