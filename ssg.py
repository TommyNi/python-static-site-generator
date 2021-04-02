import typer
import Site from ssg.Site
import os

def main(source = "content", dest = "dist"):
    config = { "source": source, "dest": dest }

    site = Site(source, dest)
    site.build()

typer.run(main)