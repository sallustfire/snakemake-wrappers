__author__ = "Connor McEntee"
__license__ = "MIT"

from snakemake.shell import shell

# all other params should be entered in "extra" param
extra = snakemake.params.get("extra", "")

bed = snakemake.input.get("bed", None)
gtf = snakemake.input.get("gtf", None)

bed_flag = "--bed %s" % bed if bed else ""
gtf_flag = "--gtf %s" % gtf if gtf else ""

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "seqkit subseq"
    " {extra}"
    " -j {snakemake.threads}"
    " {bed_flag}"
    " {gtf_flag}"
    " {snakemake.input.sequence}"
    " > {snakemake.output}"
    " {log}"
)
