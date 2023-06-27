#!/bin/env python3

from os.path import exists
import argparse
from deep_translator import GoogleTranslator


def ptrans_run() -> None:
    parser = argparse.ArgumentParser(
        description="String translation software.  \
        Google Translate is used for translation.  \
        The language must be specified by language code."
    )

    parser.add_argument("text", type=str, help="Text to be translated")

    parser.add_argument(
        "-i",
        "--input",
        default="auto",
        type=str,
        help="Language of the text before translation (default is automatic)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Language after translation (required)",
        required=True,
    )
    parser.add_argument(
        "-f",
        "--file",
        help="Used to translate files\n \
            To use, enter the file path in the text portion.",
        action="store_true",
    )
    parser.add_argument(
        "-n", "--filename", type=str, help="Name of the translated file", default=None
    )

    args = parser.parse_args()

    if args.file:
        if exists(args.text):
            filename: str = "hogehoge.txt"
            if args.filename == None:
                filename = args.text
            else:
                filename = args.filename

            tmp = ptrans_file(args.text, args.input, args.output)
            f = open(filename, "w", encoding="utf8")
            f.write(tmp)
            f.close()

            print(tmp)
            exit(0)
        else:
            print("Error: The specified file does not exist.")
            exit(0)
    else:
        print(ptrans(args.text, args.input, args.output))
        exit(0)


def ptrans(text: str, i: str, o: str) -> str:
    return GoogleTranslator(source=i, target=o).translate(text)


def ptrans_file(filename: str, i: str, o: str) -> str:
    return GoogleTranslator(source=i, target=o).translate_file(filename)


if __name__ == "__main__":
    ptrans_run()
