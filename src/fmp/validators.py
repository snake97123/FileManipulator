from pathlib import Path

ERROR_INPUT_NOT_EXISTS = "Error: input file does not exist."
ERROR_INPUT_NOT_FILE = "Error: input path is not a file."
ERROR_INPUT_NOT_READABLE = "Error: input file is not readable."
ERROR_OUTPUT_DIR_NOT_EXISTS = "Error: output directory does not exist."
ERROR_OUTPUT_IS_DIRECTORY = "Error: output path must not be a directory."
ERROR_N_INVALID = "Error: n must be greater than or equal to 1."
ERROR_NEEDLE_EMPTY = "Error: needle must not be empty."
ERROR_NEW_STRING_EMPTY = "Error: new_string must not be empty."


def validate_input_exists(input_path: Path) -> None:
    if not input_path.exists():
        raise ValueError(ERROR_INPUT_NOT_EXISTS)

def validate_input_is_file(input_path: Path) -> None:
    if not input_path.is_file():
        raise ValueError(ERROR_INPUT_NOT_FILE)

def validate_input_readable(input_path: Path) -> None:
    try:
        with input_path.open("r", encoding = "utf-8") as f:
            f.read(1)
    except OSError:
        raise ValueError(ERROR_INPUT_NOT_READABLE)

def validate_output_parent_exists(output_path: Path) -> None:
    if not output_path.parent.exists():
        raise ValueError(ERROR_OUTPUT_DIR_NOT_EXISTS)
    
def validate_output_is_not_directory(output_path: Path) -> None:
    if output_path.exists() and output_path.is_dir():
        raise ValueError(ERROR_OUTPUT_IS_DIRECTORY)

def validate_n(n: int) -> None:
    if n < 1:
        raise ValueError(ERROR_N_INVALID)

def validate_needle(needle: str) -> None:
    if needle == "":
        raise ValueError(ERROR_NEEDLE_EMPTY)

def validate_new_string(new_string: str) -> None:
    if new_string == "":
        raise ValueError(ERROR_NEW_STRING_EMPTY)

