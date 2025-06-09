"""Entry point for the command line tool."""

import typer
from rich import print
from rich.progress import track

from snake_otate.annotator_core import AnnotationCore

app = typer.Typer()
annot = AnnotationCore()

@app.command()
def annotate(): # bools are automatically options, using "" as a default value will also create a command line option
    """Initial output prior to running."""
    if annotate:
        annot.create_annotations()

@app.command()
def coverage():
    """Just a toy script to see if I understand how samtools works."""
    if coverage:
        annot.retrieve_coverage()

@app.command()
def version():
    """Print version info."""
    print("[bold magenta]snake-otate v0.1.0[/bold magenta]")

if __name__ == "__main__":
    app()