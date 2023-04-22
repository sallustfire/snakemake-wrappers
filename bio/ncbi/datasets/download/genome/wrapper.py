__author__ = "Connor McEntee"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell

accession = snakemake.params.get("accession")

# all other params should be entered in "extra" param
extra = snakemake.params.get("extra", "")

out_genome = snakemake.output.get("genome", None)
out_gff = snakemake.output.get("gff3", None)
out_cds = snakemake.output.get("cds", None)
out_protein = snakemake.output.get("protein", None)

outputs = [
    {"out": out_genome, "flag": "genome", "pattern": "%s*_genomic.fna" % accession},
    {"out": out_gff, "flag": "gff3", "pattern": "genomic.gff"},
    {"out": out_cds, "flag": "cds", "pattern": "cds_from_genomic.fna"},
    {"out": out_protein, "flag": "protein", "pattern": "protein.faa"},
]

include = ",".join((output['flag'] for output in outputs if output['out']))

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
log_extract = snakemake.log_fmt_shell(stdout=False, stderr=True, append=True)

with tempfile.NamedTemporaryFile() as tempfile:
    out_zip = tempfile.name

    shell(
        "datasets download genome"
        " accession {accession}"
        " {extra}"
        " --include {include}"
        " --filename {out_zip}"
        " --no-progressbar"
        " {log}"
    )

    for output in outputs:
        out = output['out']

        if out:
            pattern = output["pattern"]

            shell(
                "unzip "
                " -p"
                " {out_zip}"
                " 'ncbi_dataset/data/{accession}/{pattern}'"
                " > {out}"
                " {log_extract}"
            )
