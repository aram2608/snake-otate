"""Main module for annotator logic."""

from rich import print
from rich.progress import track

from snake_otate.alignments import Alignments

class AnnotationCore:
    """Core logic for creating annotations."""

    def __init__(self):
        """Base parameters."""
        self.alignments = Alignments(path="/Users/ja1473/snake-otate/examples/trimmed_0R1_S1_R1_001.fastq.gz_sorted.bam")

    def create_annotations(self):
        """Annotation logic."""
        prompt = input("Start annotation? [y/n]: ")
        if prompt == "y":
            print("[bold green] Starting annotation... [/bold green]")
            self.alignments.extract_splice_junctions()
            print("[bold cyan] Annotation complete! [/bold cyan]")
        if prompt == "n":
            print("Stopping annotation...")
