from rich.table import Table
from rich.console import Console

from config import settings

console = Console()

def show_startup_config():
    table = Table(
        title="🚀 SR2 | Configuração Inicial",
        show_header=True,
        header_style="bold cyan"
    )

    table.add_column("Config", style="bold")
    table.add_column("Valor", style="green")

    table.add_row("UDP Host", str(settings.UDP_HOST))
    table.add_row("UDP Port", str(settings.UDP_PORT))
    table.add_row("Watchdog Timeout (s)", str(settings.WATCHDOG_TIMEOUT))
    table.add_row("Export Interval (s)", str(settings.EXPORT_INTERVAL))
    table.add_row("Telemetry Fields", ", ".join(settings.TELEMETRY_FIELDS))

    console.print(table)
