"""Entry point for the command line tool."""

import typer
from rich import print
from rich.progress import track
import time

app = typer.Typer()

@app.command()
def annotate(): # bools are automatically options, using "" as a default value will also create a command line option
    """Initial output prior to running."""
    if annotate:
        print("[bold green] Starting annotation... [/bold green]")
        for i in track(range(5), description="Processing..."):
            time.sleep(1)
        print("[bold cyan] Annotation complete! [/bold cyan]")

@app.command()
def version():
    """Print version info."""
    print("[bold magenta]snake-otate v0.1.0[/bold magenta]")

if __name__ == "__main__":
    typer.run(main)