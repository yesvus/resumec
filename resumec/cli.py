import typer
from resumec.pipeline.orchestrator import compile_cv

app = typer.Typer(help="Resumec: Deterministic CV compiler pipeline.")

@app.callback()
def callback():
    pass

@app.command()
def compile(job_url: str):
    """
    Compiles a raw CV against the given remote job description URL.
    """
    compile_cv(job_url)

if __name__ == "__main__":
    app()
