#!/usr/bin/env python3
"""
pt2py - Traduz arquivos Pitão (.pt) para Python (.py)
"""

import argparse
import os

from pitao import parser
from pitao.logger import Logger
from pitao import VERSION_NUMBER


def main():
    """Main entry point for the pt2py command."""
    argparser = argparse.ArgumentParser(
        "pt2py",
        description="Traduz arquivos Pitão (.pt) para Python (.py)",
        formatter_class=argparse.RawTextHelpFormatter
    )
    argparser.add_argument(
        "-V", "--version",
        action="version",
        version=f"pt2py (Pitão v{VERSION_NUMBER})"
    )
    argparser.add_argument(
        "-v", "--verbose",
        help="imprime progresso",
        action="store_true"
    )
    argparser.add_argument(
        "-o", "--output",
        type=str,
        help="especifica nome do arquivo de saída",
        nargs=1
    )
    argparser.add_argument(
        "input",
        type=str,
        help="arquivos Pitão para traduzir",
        nargs="+"
    )

    cmd_args = argparser.parse_args()
    logger = Logger(cmd_args.verbose)

    for input_file in cmd_args.input:
        if not os.path.isfile(input_file):
            logger.log_error(f"Arquivo não encontrado: '{input_file}'")
            continue

        logger.log_info(f"Traduzindo '{input_file}'")

        outputname = cmd_args.output[0] if cmd_args.output else None

        try:
            output_path = parser.parse_file(input_file, "", outputname, None)
            logger.log_info(f"Criado '{output_path}'")
        except Exception as e:
            logger.log_error(f"Erro ao traduzir '{input_file}': {str(e)}")


if __name__ == '__main__':
    main()
