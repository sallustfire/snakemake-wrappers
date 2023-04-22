__author__ = "Connor McEntee"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell

accession = snakemake.params.get("accession")

# all other params should be entered in "extra" param
extra = snakemake.params.get("extra", "")

out_gene = snakemake.output.get("gene", None)
out_rna = snakemake.output.get("rna", None)
out_protein = snakemake.output.get("protein", None)
out_cds = snakemake.output.get("cds", None)
out_5p_utr = snakemake.output.get("5p-utr", None)
out_3p_utr = snakemake.output.get("3p-utr", None)
out_product_report = snakemake.output.get("product-report", None)

outputs = [
    {"out": out_gene, "flag": "gene", "pattern": "gene.fna"},
    {"out": out_rna, "flag": "rna", "pattern": "rna.fna"},
    {"out": out_protein, "flag": "protein", "pattern": "protein.faa"},
    {"out": out_cds, "flag": "cds", "pattern": "cds.fna"},
    {"out": out_5p_utr, "flag": "5p-utr", "pattern": "5p_utr.gff"},
    {"out": out_3p_utr, "flag": "3p-utr", "pattern": "3p_utr.gff"},
    {"out": out_product_report, "flag": "product-report", "pattern": "product_report.jsonl"},
]

include = ",".join((output['flag'] for output in outputs if output['out']))

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
log_extract = snakemake.log_fmt_shell(stdout=False, stderr=True, append=True)

with tempfile.NamedTemporaryFile() as tempfile:
    out_zip = tempfile.name

    shell(
        "datasets download gene"
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
                " 'ncbi_dataset/data/{pattern}'"
                " > {out}"
                " {log_extract}"
            )
