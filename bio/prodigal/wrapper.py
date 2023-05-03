__author__ = "Connor McEntee"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

procedure = snakemake.params.get("procedure", "single")

# all other params should be entered in "extra" param
extra = snakemake.params.get("extra", "")

out = snakemake.output.get("gff")
out_faa = snakemake.output.get("faa")
out_fna = snakemake.output.get("fna")

faa_flag = "-a %s" % out_faa if out_faa else ""
fna_flag = "-d %s" % out_fna if out_fna else ""

(out_name, ext) = path.splitext(out)

out_format = None
if ext.startswith(".gff") or ext.startswith(".gff3"):
    out_format = "gff"
elif ext.startswith(".gbk"):
    out_format = "gbk"
elif ext.startswith(".sco"):
    out_format = "sco"

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "prodigal"
    " {extra}" 
    " -p {procedure}"
    " -i {snakemake.input.fna}"
    " {faa_flag}"
    " {fna_flag}"
    " -f {out_format}"
    " -o {out}"
    " {log}"
)
