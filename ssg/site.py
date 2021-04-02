import Path from pathlib
import os

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = Path(self.dest / path.relative_to(self.source))
        os.mkdir(directory, parents=True, exist_ok=True)

    def build()
        os.mkdir(self.dest, parents=True)
        for path in self.source.rglob("*"):
            if path is Path.directory:
                self.create_dir(path)


        