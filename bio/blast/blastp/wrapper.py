__author__ = "Connor McEntee"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

remote_db = snakemake.params.get("remoteDB", None)
format = snakemake.params.get("format", None)

if remote_db:
    db_flag = "-db {} -remote".format(remote_db)
else:
    blastdb = snakemake.input.get("blastdb")[0]
    db_name = path.splitext(blastdb)[0]

    db_flag = "-db {} -num_threads {}".format(db_name, snakemake.threads)

if format:
    out_format = "-outfmt '{}'".format(format)

shell(
    "blastp"
    " -query {snakemake.input.query}"
    " {out_format}"
    " {snakemake.params.extra}"
    " {db_flag}"
    " -out {snakemake.output[0]}"
    " {log}"
)
