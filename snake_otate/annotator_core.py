"""Main module for annotator logic."""

from rich import print
from rich.progress import track

from snake_otate.alignments import Alignments

class AnnotationCore:
    """Core logic for creating annotations."""

    def __init__(self):
        """Base parameters."""
        self.path = "/Users/ja1473/snake-otate/examples/trimmed_0R1_S1_R1_001.fastq.gz_sorted.bam"
        self.alignments = Alignments(path=self.path)

    def create_annotations(self):
        """Annotation logic."""
        prompt = input("Start annotation? [y/n]: ")
        if prompt == "y":
            print("[bold green] Starting annotation... [/bold green]")
            self.alignments.extract_splice_junctions()
            print("[bold cyan] Annotation complete! [/bold cyan]")
        if prompt == "n":
            print("[bold red] Stopping annotation... [/bold red]")

    def retrieve_counts(self):
        prompt = input("Return coverage? [y/n]: ")
        if prompt == "y":
            print(f"[bold yellow] Retrieving coverage from {self.path} [/bold yellow]")
            self.alignments.read_count_per_region()
        if prompt == "n":
            print("[bold red] Stopping retrieval [/bold red]")
