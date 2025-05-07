import typer
import importlib
import pkgutil
from cavum.plugins import __path__ as plugin_path

app = typer.Typer(help="Cavum: Linux memory forensics framework")

def load_plugins():
    """
    Dynamically discover and register CLI plugins from the cavum.plugins package.
    Each plugin must define a `cli: typer.Typer` object.
    """
    for _, module_name, _ in pkgutil.iter_modules(plugin_path):
        try:
            mod = importlib.import_module(f"cavum.plugins.{module_name}")
            if hasattr(mod, "cli") and isinstance(mod.cli, typer.Typer):
                app.add_typer(mod.cli, name=module_name)
            else:
                typer.secho(f"[WARN] Plugin '{module_name}' has no `cli: Typer` object.", fg=typer.colors.YELLOW)
        except Exception as e:
            typer.secho(f"[ERROR] Failed to load plugin '{module_name}': {e}", fg=typer.colors.RED)

# Initialize plugins at runtime
load_plugins()

