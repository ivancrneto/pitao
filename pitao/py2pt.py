#!/usr/bin/env python3
"""
py2pt - Traduz arquivos Python (.py) para Pitão (.pt)
"""

import argparse
import os

from pitao import parser
from pitao.logger import Logger
from pitao import VERSION_NUMBER


def main():
    """Main entry point for the py2pt command."""
    argparser = argparse.ArgumentParser(
        "py2pt",
        description="Traduz arquivos Python (.py) para Pitão (.pt)",
        formatter_class=argparse.RawTextHelpFormatter
    )
    argparser.add_argument(
        "-V", "--version",
        action="version",
        version=f"py2pt (Pitão v{VERSION_NUMBER})"
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
        help="arquivos Python para traduzir",
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
            output_path = parser.reverse_parse_file(input_file, "", outputname)
            logger.log_info(f"Criado '{output_path}'")
        except Exception as e:
            logger.log_error(f"Erro ao traduzir '{input_file}': {str(e)}")


if __name__ == '__main__':
    main()
