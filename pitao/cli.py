#!/usr/bin/env python3
"""
Pitão - Python com palavras reservadas em Português

Este é o utilitário principal para traduzir e executar arquivos Pitão.
"""

import argparse
import os
import sys

from pitao import parser
from pitao.logger import Logger
from pitao import VERSION_NUMBER


def main():
    """Main entry point for the pitao command."""
    # Setup argument parser
    argparser = argparse.ArgumentParser(
        "pitao",
        description="Pitão é um preprocessador Python que traduz palavras reservadas em Português para Inglês",
        formatter_class=argparse.RawTextHelpFormatter
    )
    argparser.add_argument(
        "-V", "--version",
        action="version",
        version=f"Pitão v{VERSION_NUMBER}"
    )
    argparser.add_argument(
        "-v", "--verbose",
        help="imprime progresso",
        action="store_true"
    )
    argparser.add_argument(
        "-c", "--compile",
        help="traduz para Python apenas (não executa)",
        action="store_true"
    )
    argparser.add_argument(
        "-k", "--keep",
        help="mantém arquivos Python gerados",
        action="store_true"
    )
    argparser.add_argument(
        "-2", "--python2",
        help="usa python2 ao invés de python3 (padrão)",
        action="store_true"
    )
    argparser.add_argument(
        "-o", "--output",
        type=str,
        help="especifica nome do arquivo de saída (com -c)",
        nargs=1
    )
    argparser.add_argument(
        "input",
        type=str,
        help="arquivos Pitão para processar",
        nargs=1
    )
    argparser.add_argument(
        "args",
        type=str,
        help="argumentos para o script",
        nargs=argparse.REMAINDER
    )

    # Parse arguments
    cmd_args = argparser.parse_args()

    # Create logger
    logger = Logger(cmd_args.verbose)

    # Check for invalid combination of flags
    if cmd_args.output is not None and cmd_args.compile is False:
        logger.log_error("Não é possível especificar saída quando Pitão não está em modo de compilação")
        sys.exit(1)

    # Where to output files
    if cmd_args.compile or cmd_args.keep:
        path_prefix = ""
        logger.log_info("Colocando arquivos neste diretório")
    else:
        path_prefix = "python_"
        logger.log_info("Colocando arquivos neste diretório com prefixo python_*")

    # List of all files to translate from Pitão to Python
    parse_queue = []

    # Add all files from cmd line
    parse_queue.append(cmd_args.input[0])
    if cmd_args.compile:
        for arg in cmd_args.args:
            parse_queue.append(arg)

    # Add all files from imports recursively
    logger.log_info("Procurando por importações")
    i = 0
    while i < len(parse_queue):
        try:
            import_files = parser.parse_imports(parse_queue[i])
        except FileNotFoundError:
            logger.log_error(f"Arquivo não encontrado: '{parse_queue[i]}'")
            sys.exit(1)

        for import_file in import_files:
            if os.path.isfile(import_file) and import_file not in parse_queue:
                logger.log_info(f"Adicionando '{import_file}' à fila de processamento")
                parse_queue.append(import_file)

        i += 1

    if path_prefix != "":
        import_translations = {}
        for file in parse_queue:
            import_translations[file[:-3]] = path_prefix + file[:-3]
    else:
        import_translations = None

    # Parsing
    generated_files = []
    current_file_name = None
    try:
        for file in parse_queue:
            current_file_name = file
            logger.log_info(f"Processando '{file}'")

            if cmd_args.output is None:
                outputname = None
            elif os.path.isdir(cmd_args.output[0]):
                new_file_name = parser._change_file_name(os.path.split(file)[1])
                outputname = os.path.join(cmd_args.output[0], new_file_name)
            else:
                outputname = cmd_args.output[0]

            output_path = parser.parse_file(
                file,
                path_prefix,
                outputname,
                import_translations
            )
            generated_files.append(output_path)

    except (TypeError, FileNotFoundError) as e:
        logger.log_error(f"Erro ao processar '{current_file_name}'.\n{str(e)}")
        # Cleanup
        for gen_file in generated_files:
            try:
                os.remove(gen_file)
            except:
                pass
        sys.exit(1)

    # Stop if we were only asked to translate
    if cmd_args.compile:
        return

    # Run file
    python_command = "python2" if cmd_args.python2 else "python3"

    filename = os.path.basename(cmd_args.input[0])
    output_file = os.path.join(
        os.path.dirname(cmd_args.input[0]) or ".",
        path_prefix + parser._change_file_name(filename, None)
    )

    try:
        logger.log_info("Executando")
        logger.program_header()
        os.system(
            f"{python_command} {output_file} {' '.join(cmd_args.args)}"
        )
        logger.program_footer()

    except Exception as e:
        logger.log_error("Erro inesperado ao executar Python")
        logger.log_info(f"Mensagem de erro: {str(e)}")

    # Delete files if not keeping
    if not cmd_args.keep:
        logger.log_info("Deletando arquivos temporários")
        for gen_file in generated_files:
            try:
                os.remove(gen_file)
            except:
                logger.log_error(f"Não foi possível deletar '{gen_file}'")


if __name__ == '__main__':
    main()
