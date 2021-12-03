# MBB659Termproject

MBB659 Final Project: Alignment and annotation pipeline for Klebsiella pneumoniae

Project background

Klebsiella pneumoniae is considered by World Health Organization as a critical priority pathogen that urgently needs new antibiotic treatment, as it is highly resistant to most antibiotics and encodes a diverse set of antimicrobial resistance (AMR) genes that can be easily transmitted between different </var>bacteria<sup>1,2</sup>. Of great concern is K. pneumoniae’s role in trafficking AMR genes on a global scale3. Recently, in addition to the reservoir of AMR genes, extended spectrum beta lactamase (ESBL) genes carried by many of these clonal groups have further hindered the effects of last-line-of-defence antibiotics used in treatment4. As a opportunistic pathogen linked to many nosocomial outbreaks, K. pneumoniae’s fits a niche where there is constant selective pressure from exposure to antibiotics5. The pathogenicity of K. pneumoniae is not only linked to the hospital setting. There are strains of hypervirulent K. pneumoniae (hvkp) that cause community-linked outbreaks6. These are often less resistant compared to their relative AMR strains. These hvkp strains are found with thicker capsules to evade host immune mechanisms. however, there has been a rise in detection of ESBL genes carried in hvkp6,7. I hypothesize that hvkp strains of K. pneumoniae containing ESBL resistance likely have higher mutations and genetic variants in capsule genes, such as rmpA, that contributes to the intake of ESBL on plasmids.

The steps for this pipeline are:

1. Download reference genome and reads <b>SRA_toolkit</b>
2. Align reads to the reference genome <b>bwa mem</b>
3. Call variants and manipulate <b>bcftools</b>
4. Gene annotation <b>snpEff</b>



Directed Acyclic Graph:

![image](https://user-images.githubusercontent.com/83785437/144008656-4c6c9095-77c9-416e-8b81-122b0311f250.png)

Heres how to access the git:

Cloning the repository:

Create folder where you want the repo

Open terminal in that folder

In terminal enter:
git clone https://github.com/kluongni/MBB659Termproject.git

<p>Then activate the conda environment with:
  conda env create --file environment.yml
  (press y when prompted)
  conda activate termProject</p>
  
Run the Snakemake file with:
snakemake --cores * "results/annotatedVcf.vcf" will bring you to the end of the pipeline
*designates amount of cores user would like to dedicate,  

Inputs:

GCA_000009885.1_ASM988v1 is a hvkp whole-genome assembly used as a reference genome for alignment.
SRR10160941 is the SRA accession for a Illumina High-throughput sequenced carbapenemase carrying hvkp.

Outputs:

snpEff_genes.txt is a text file containing the gene annotation.

annotatedVcf.vcf is a annotated vcf file of all the genes found within the sequence that was aligned.


The snpEFF_genes.txt provides valuable information on 
Further analyses of my pipeline showed that contrary to my hypothesis, there were no significant amount of genetic variations in the rmpA gene that I believed would lead to ESBL acquisition.


![image](https://user-images.githubusercontent.com/83785437/144008573-c04a5939-cf96-4e3e-8569-6341368b8465.png)







References:
1.	Navon-Venezia, S., Kondratyeva, K. & Carattoli, A. Klebsiella pneumoniae: a major worldwide source and shuttle for antibiotic resistance. FEMS Microbiol. Rev. 013, 252–275 (2017).
2.	Sands, K. et al. Characterization of antimicrobial-resistant Gram-negative bacteria that cause neonatal sepsis in seven low- and middle-income countries. Nat. Microbiol. 23, 24.
3.	Wyres, K. L. & Holt, K. E. Klebsiella pneumoniae as a key trafficker of drug resistance genes from environmental to clinically important bacteria. Curr. Opin. Microbiol. 45, 131–139 (2018).
4.	Chiu, S. K. et al. Carbapenem Nonsusceptible Klebsiella pneumoniae in Taiwan: Dissemination and Increasing Resistance of Carbapenemase Producers During 2012-2015. Sci. Rep. 8, 1–9 (2018).
5.	Anes, J., Hurley, D., Martins, M. & Fanning, S. Exploring the Genome and Phenotype of Multi-Drug Resistant Klebsiella pneumoniae of Clinical Origin. Front. Microbiol 8, (2017).
6.	Lee, C. R. et al. Antimicrobial resistance of hypervirulent Klebsiella pneumoniae: Epidemiology, hypervirulence-associated determinants, and resistance mechanisms. Front. Cell. Infect. Microbiol. 7, (2017).
7.	Xie, M. et al. Clinical evolution of ST11 carbapenem resistant and hypervirulent Klebsiella pneumoniae. Commun. Biol. 4, 1–9 (2021).

