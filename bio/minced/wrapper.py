__author__ = "Connor McEntee"
__license__ = "MIT"

from snakemake.shell import shell

# all other params should be entered in "extra" param
extra = snakemake.params.get("extra", "")

gff = snakemake.output.get("gff")
text = snakemake.output.get("text", "")
spacers = snakemake.output.get("spacers", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "minced"
    " -gff"
    " {extra}"
    " {snakemake.input}"
    " {text}"
    " {gff}"
    " {log}"
)
