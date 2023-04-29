__author__ = "Connor McEntee"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
extra = snakemake.params.get("extra", "")
shift = snakemake.params.get("shift")

shift_flag = "-s %d" % shift if shift or shift == 0 else ""

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "bedtools shift"
    " {extra}"
    " {shift_flag}"
    " -i {snakemake.input.input}"
    " -g {snakemake.input.genome}"
    " > {snakemake.output}"
    " {log}"
)
