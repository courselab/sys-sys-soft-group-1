#    SPDX-FileCopyrightText: 2024 AlvaroJoseLopes <alvarojoselopes@hotmail.com>
#
#    SPDX-License-Identifier: GPL-3.0-or-later

# hwasm.py

import sys

registerCodes = {"ah": b"\xB4", "al": b"\xB0"}
opCodes = {"mov": b"\xB0", "int": b"\xCD", "hlt": b"\xF4", "jmp": b"\xEB\xFD"}


def get_args(tokens: list[str]) -> str:
    return " ".join(tokens[1:])


def pre_process_arg(arg: str) -> str:
    return arg.strip().replace("$", "").replace("%", "")


def mov(tokens: list[str]) -> bytes:
    args = get_args(tokens)
    source, destination = [pre_process_arg(arg) for arg in args.split(",")]

    if source.startswith("0"):
        source = int(source, 16)
        source = bytes([source])
    elif source.startswith("'"):
        source = source.replace("'", "")
        source = source.encode("utf-8")

    destination = registerCodes[destination]

    return destination + source


def interrupt(tokens: list[str]) -> bytes:
    timeout = pre_process_arg(get_args(tokens))
    timeout = int(timeout, 16)

    return opCodes["int"] + bytes([timeout])


def word(tokens: list[str]) -> bytes:
    return b"\x55\xAA"


def main(input_file):
    with open(input_file, "r") as f:
        file_content = f.readlines()

    binary_code = bytearray()
    for line in file_content:
        line = line.strip().split("#")[0].strip()
        if not line:
            continue

        tokens = line.split()
        match tokens[0]:
            case "#":
                continue
            case "mov":
                binary_code += mov(tokens)
            case "int":
                binary_code += interrupt(tokens)
            case "hlt":
                binary_code += opCodes["hlt"]
            case "jmp":
                binary_code += opCodes["jmp"]
            case ".word":
                binary_code += word(tokens)
            case ".fill":
                binary_code += bytes(461)
            case _:
                continue

    with open("hw.bin", "wb") as f:
        f.write(binary_code)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage python3 hwasm.py <.ASM file>")
        exit(0)
    main(*sys.argv[1:])
