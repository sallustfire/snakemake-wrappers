__author__ = "Connor McEntee"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

def main_output_flag(output):
    if not output:
        return ""

    (name, ext) = path.splitext(output)
    if ext.startswith(".gff") or ext.startswith(".gff3"):
        return "-o %s" % output
    elif ext.startswith(".gtf"):
        return "-T -o %s" % output
    elif ext.startswith(".bed"):
        return "--bed -o %s" % output

# all other params should be entered in "extra" param
extra = snakemake.params.get("extra", "")

input_records = snakemake.input.get("records")
input_sequence = snakemake.input.get("sequence", None)
input_ids = snakemake.input.get("ids", None)

sequence_flag = "-g %s" % input_sequence if input_sequence else ""
ids_flag = "--ids %s" % input_ids if input_ids else ""

out_records = snakemake.output.get("records")
out_faa = snakemake.output.get("faa")
out_fna = snakemake.output.get("fna")

out_flag = main_output_flag(out_records)
faa_flag = "-y %s" % out_faa if out_faa else ""
fna_flag = "-x %s" % out_fna if out_fna else ""

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "gffread"
    " {extra}"
    " {input_records}"
    " {ids_flag}"
    " {sequence_flag}"
    " {out_flag}"
    " {faa_flag}"
    " {fna_flag}"
    " {log}"
)
