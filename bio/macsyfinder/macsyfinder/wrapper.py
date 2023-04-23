__author__ = "Connor McEntee"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

# all other params should be entered in "extra" param
extra = snakemake.params.get("extra", "")
db_type = snakemake.params.get("db_type", "unordered")
models = snakemake.params.get("models", "all")

sequence_db = snakemake.input.get("sequence_db")
models_dir = snakemake.input.get("models")

out = snakemake.output[0]

(outdir, basename) = path.split(out)

models_dir_flag = "--models-dir %s" % models_dir if models_dir else ""

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Validate that macsyfinder has a non-empty input, it panics otherwise
if not path.getsize(sequence_db):
    raise ValueError("Cannot process empty sequence_db")

# Clear the output directory before executing
shell("rm -rf {outdir}")
shell(
    "macsyfinder"
    " {extra}"
    " -w {snakemake.threads}"
    " --db-type {db_type}"
    " --models {models}"
    " {models_dir_flag}"
    " --sequence-db {sequence_db}"
    " -o {outdir}"
    " {log}"
)

# Remove the hmmer_results folder which are really just intermediate outputs
out_hmmer_results = path.join(outdir, "hmmer_results")
shell("rm -rf {out_hmmer_results}")
