# minecli is a collection of minecraft server utilities
# Copyright (C) 2020  Manuel Quarneti

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import importlib
from os import path
import pathlib
import click
import appdirs


@click.group()
def cli():
    pass


@cli.group()
def server():
    pass


@server.command()
@click.argument("name", required=True)
@click.option(
    "--servertype", default="vanilla", help="The server type (vanilla/spigot/paper)"
)
def create(name, servertype):
    """Create a server"""
    basedir = appdirs.user_data_dir(appname="mclib", appauthor=False, roaming=True)
    serverdir = path.join(basedir, name)
    pathlib.Path(serverdir).mkdir(parents=True, exist_ok=True)

    server_module = importlib.import_module(f"minelib.server.{servertype}")
    server = server_module.MinecraftServer(serverdir)
    server.download()

    print(f"{name} created at {serverdir}")


if __name__ == "__main__":
    cli()
