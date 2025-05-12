import typer

app = typer.Typer(help="TrackWise - Your spending tracker")

@app.command()
def hello():
    """Hello command"""
    typer.echo("Welcome to TrackWise!")

if __name__ == "__main__":
    app()