import typer
from pathlib import Path

from validators import (
    validate_input_exists,
    validate_input_is_file,
    validate_input_readable,
    validate_output_parent_exists,
    validate_output_is_not_directory,
    validate_n,
    validate_needle,
    validate_new_string
)

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}!")

@app.command()
def reverse(input_path: Path, output_path: Path) -> None:
    try:
        validate_input_exists(input_path)
        validate_input_is_file(input_path)
        validate_input_readable(input_path)
        validate_output_parent_exists(output_path)
        validate_output_is_not_directory(output_path)
    
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()

        reversed_text = text[::-1]

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(reversed_text)
    except ValueError as e:
        typer.echo(str(e))
        raise typer.Exit(code=1)
    

@app.command()
def copy(input_path: Path, output_path: Path) -> None:
    try:
        validate_input_exists(input_path)
        validate_input_is_file(input_path)
        validate_input_readable(input_path)
        validate_output_parent_exists(output_path)
        validate_output_is_not_directory(output_path)
        
        with open(input_path, "r", encoding="utf-8") as f:
                text = f.read()
    
        with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
        
    except ValueError as e:
        typer.echo(str(e))
        raise typer.Exit(code=1)

@app.command()
def duplicate(input_path: Path, n: int) -> None:
    try:
        validate_input_exists(input_path)
        validate_input_is_file(input_path)
        validate_input_readable(input_path)
        validate_n(n)
    
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()
            duplicated_text = text * n

        with open(input_path, "w", encoding="utf-8") as f:
            f.write(duplicated_text)

    except ValueError as e:
        typer.echo(str(e))
        raise typer.Exit(code=1)

@app.command()
def replace(input_path: Path, needle: str, new_string: str) -> None:
    try:
        validate_input_exists(input_path)
        validate_input_is_file(input_path)
        validate_input_readable(input_path)
        validate_needle(needle)
        validate_new_string(new_string)
        
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()
            replaced_text = text.replace(needle, new_string)
    
        with open(input_path, "w", encoding="utf-8") as f:
            f.write(replaced_text)
    except ValueError as e:
        typer.echo(str(e))
        raise typer.Exit(code=1)

if __name__ == "__main__":
    # typer.run(hello)
    app()