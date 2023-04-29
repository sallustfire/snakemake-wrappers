__author__ = "Connor McEntee"
__license__ = "MIT"

import os
from snakemake.shell import shell

out_prefix = snakemake.params.get("out_prefix", "bin")

# all other params should be entered in "extra" param
extra = snakemake.params.get("extra", "")

input_abd = snakemake.input.get("abd")

abd_flag = "-a %s" % input_abd if input_abd else ""

output_dir = snakemake.output[0]
output_prefix = os.path.join(output_dir, out_prefix)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "metabat2"
    " {extra}"
    " -t {snakemake.threads}"
    " -i {snakemake.input.input}"
    " {abd_flag}"
    " -o {output_prefix}"
    " {log}"
)
