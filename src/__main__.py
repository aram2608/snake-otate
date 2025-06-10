"""Entry point for the command line tool."""

import typer
from rich import print
from rich.progress import track

from src.annotator_core import AnnotationCore

app = typer.Typer()
annot = AnnotationCore()

@app.command()
def test():
    if test:
        annot.dummy()

@app.command()
def annotate(): # bools are automatically options, using "" as a default value will also create a command line option
    """Initial output prior to running."""
    if annotate:
        annot.create_annotations()

@app.command()
def region_coverage():
    """Just a toy script to see if I understand how samtools works."""
    if region_coverage:
        annot.retrieve_counts()

@app.command()
def version():
    """Print version info."""
    print("[bold magenta]snake-otate v0.1.0[/bold magenta]")

if __name__ == "__main__":
    app()