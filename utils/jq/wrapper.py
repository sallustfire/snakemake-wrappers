__author__ = "Connor McEntee"
__license__ = "MIT"

from snakemake.shell import shell

# all other params should be entered in "extra" param
extra = snakemake.params.get("extra", "")
filter_value = snakemake.params.get("filter")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "jq"
    " {extra}"
    " '{filter_value}'"
    " {snakemake.input}"
    " > {snakemake.output}"
    " {log}"
)
