__author__ = "Connor McEntee"
__license__ = "MIT"

from snakemake.shell import shell

accession = snakemake.params.get("accession")

# all other params should be entered in "extra" param
extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "datasets summary genome"
    " accession {accession}"
    " {extra}"
    " > {snakemake.output}"
    " {log}"
)
