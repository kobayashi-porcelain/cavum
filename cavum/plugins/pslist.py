# cavum/plugins/pslist.py
import typer

cli = typer.Typer(help="List active processes from memory image")

@cli.command("run")
def run_pslist(image: str = typer.Option(..., help="Path to memory image")):
    typer.echo(f"[pslist] would analyze: {image}")
    # Placeholder: integrate with cavum.core.memory_reader

