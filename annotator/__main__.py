"""Entry point for the command line tool."""

import typer

def main(annotate: bool = False):
    """Initial output prior to running."""
    if annotate:
        print("Starting annotation...")

if __name__ == "__main__":
    typer.run(main)