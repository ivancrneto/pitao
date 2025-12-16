"""
Simple logging utility for Pitão.
"""


class Logger:
    """
    Logger class for printing progress and error messages.
    """

    def __init__(self, verbose=False):
        """
        Initialize logger.

        Args:
            verbose (bool): Whether to print info messages
        """
        self.verbose = verbose

    def log_info(self, message):
        """
        Print info message if verbose mode is enabled.

        Args:
            message (str): Message to print
        """
        if self.verbose:
            print(f"[INFO] {message}")

    def log_error(self, message):
        """
        Print error message (always shown).

        Args:
            message (str): Error message to print
        """
        print(f"[ERRO] {message}")

    def program_header(self):
        """Print header before program output."""
        if self.verbose:
            print("-" * 50)

    def program_footer(self):
        """Print footer after program output."""
        if self.verbose:
            print("-" * 50)
