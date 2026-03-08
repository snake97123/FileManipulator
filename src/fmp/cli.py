import typer
from pathlib import Path

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}!")

@app.command()
def reverse(input_path: Path, output_path: Path) -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    reversed_text = text[::-1]

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(reversed_text)

@app.command()
def copy(input_path: Path, output_path: Path) -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

@app.command()
def duplicate(input_path: Path, n: int) -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()
        duplicated_text = text * n

    with open(input_path, "w", encoding="utf-8") as f:
        f.write(duplicated_text)

@app.command()
def replace(input_path: Path, needle: str, new_string: str) -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()
        replaced_text = text.replace(needle, new_string)
    
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(replaced_text)

if __name__ == "__main__":
    # typer.run(hello)
    app()