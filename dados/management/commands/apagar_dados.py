from django.core.management import BaseCommand
from django.db import connection, transaction


class Command(BaseCommand):
    help = "Redefine o sistema, apagando tudo(dados) do banco"

    @transaction.atomic
    def handle(self, *args, **options):
        cursor = connection.cursor()

        app_label = ["alimentos", "exigencias", "animais"]
        tables = [
            table
            for table in connection.introspection.table_names()
            if any(app in table for app in app_label)
        ]

        for table in tables:
            cursor.execute(f'TRUNCATE TABLE "{table}" RESTART IDENTITY CASCADE')

        self.stdout.write(self.style.WARNING("Banco de dados limpo com sucesso!"))