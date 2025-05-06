import typer
import importlib
import pkgutil
from cavum.plugins import __path__ as plugin_path

app = typer.Typer(help="Cavum: Linux memory forensics framework")

# Dynamically load plugins from cavum.plugins
def load_plugins():
    for _, module_name, _ in pkgutil.iter_modules(plugin_path):
        try:
            mod = importlib.import_module(f"cavum.plugins.{module_name}")
            if hasattr(mod, "cli") and isinstance(mod.cli, typer.Typer):
                app.add_typer(mod.cli, name=module_name)
        except Exception as e:
            typer.secho(f"Failed to load plugin '{module_name}': {e}", fg=typer.colors.RED)

load_plugins()

