__author__ = "Connor McEntee"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "hmmfetch"
    " -o {snakemake.output}"
    " {snakemake.input}"
    " {snakemake.params.key}"
    " {log}"
)
