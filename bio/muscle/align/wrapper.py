__author__ = "Connor McEntee"
__license__ = "MIT"

from snakemake.shell import shell

# all other params should be entered in "extra" param
extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "muscle"
    " {extra}"
    " -threads {snakemake.threads}"
    " -align {snakemake.input.fasta} "
    " -output {snakemake.output.alignment} "
    " {log}"
)