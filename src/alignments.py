"""Module for alignment handling."""

import pysam
from rich import print

class Alignments:
    """Class for handling all alignment tools."""
    def __init__(self, path):
        self.path = path

    def extract_splice_junctions(self):
        """Function to extract splice junctions from a BAM file."""
        bamfile = pysam.AlignmentFile(self.path, "rb") # mode = rb, reading and compressed, wb writing and compressed
        for pileupcolumn in bamfile.pileup("CM052345.1", 0, 5000):
            print("[bold blue]\ncoverage at base %s = %s [/bold blue]" % (pileupcolumn.pos, pileupcolumn.n))
            for pileupread in pileupcolumn.pileups:
                if not pileupread.is_del and not pileupread.is_refskip:
                    # query position is None if is_del or is_refskip is set.
                    print('[bold blue] \tbase in read %s = %s [/bold blue]' %
                        (pileupread.alignment.query_name,
                        pileupread.alignment.query_sequence[pileupread.query_position]))
        bamfile.close()

    def read_count_per_region(self):
        """Retrieve coverage."""
        bamfile = pysam.AlignmentFile(self.path, "rb")
        print(bamfile.count("CM052345.1"))
        bamfile.close()