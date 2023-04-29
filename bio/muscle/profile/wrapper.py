__author__ = "Connor McEntee"
__license__ = "MIT"

from snakemake.shell import shell

# all other params should be entered in "extra" param
extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "muscle"
    " {extra}"
    " -profile"
    " -in1 {snakemake.input[0]}"
    " -in2 {snakemake.input[1]}"
    " -out {snakemake.output[0]}"
    "{log}"
)
