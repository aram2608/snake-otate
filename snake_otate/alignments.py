"""Module for alignment handling."""

import pysam

class Alignments:
    """Class for handling all alignment tools."""
    def __init__(self, path):
        self.path = path

    def extract_splice_junctions(self):
        """Function to extract splice junctions from a BAM file."""
        bamfile = pysam.AlignmentFile(self.path, "rb") # mode = rb, reading and compressed, wb writing and compressed
        iter = bamfile.fetch()
        debugging_stop = []
        for i in iter:
            print(str(i))
            debugging_stop.append(i)
            if len(debugging_stop) == 10:
                break