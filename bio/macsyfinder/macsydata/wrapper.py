__author__ = "Connor McEntee"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

models = snakemake.params.get("models")
out = snakemake.output[0]

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "macsydata install"
    " -f"
    " -t {out}"
    " {models}"
    " {log}"
)
