import re
import tomlkit
from pathlib import Path
from argparse import ArgumentParser


def main():
    parse = ArgumentParser(
                prog="Spacesuit",
                description='Makes it easier to switch between themes in Starship'
                )
    parse.add_argument('Name', action='store')
    theme = parse.parse_args()
    theme = theme.Name
    text = ""
    with open(str(Path.home())+"/.config/starshipthemes/"+str(theme)+".toml", "r+", encoding="utf-8") as f:
        text = f.read()
    tomldata = tomlkit.parse(text.strip())
    starfile = ""
    with open(str(Path.home())+"/.config/starshipthemes/template.toml", "r+", encoding="utf-8") as f:
        starfile = f.read()
    for key in tomldata.keys():
        starfile = re.sub(str(key)+"([^\\]])", str(tomldata[key])+"\'", starfile)
    with open(str(Path.home())+"/.config/starship.toml", "w+", encoding="utf-8") as f:
        f.write(starfile)


if __name__ == "__main__":
    main()
