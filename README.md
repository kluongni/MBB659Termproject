# MBB659Termproject

MBB659 Final Project: Alignment and annotation pipeline for *Klebsiella pneumoniae*

# Project background

*Klebsiella pneumoniae* is considered by World Health Organization as a critical priority pathogen that urgently needs new antibiotic treatment, as it is highly resistant to most antibiotics and encodes a diverse set of antimicrobial resistance (AMR) genes that can be easily transmitted between different bacteria<sup>1,2</sup>. Of great concern is *K. pneumoniae*’s role in trafficking AMR genes on a global scale<sup>3</sup>. Recently, in addition to the reservoir of AMR genes, carbapenemase genes carried by many large plasmid have further hindered the effects of last-line-of-defence antibiotics used in treatment<sup>4</sup>. Furthermore, *K. pneumoniae* is a natural inhabitant of the gastrointestinal microbiome and an important pathogen in nosocomial infections<sup>2</sup>. There are strains of hypervirulent *K. pneumoniae* (hvkp) that cause these community-linked outbreaks<sup>6</sup>. However, it is observed these are often less resistant compared to AMR strains. These hvkp strains are found to have thicker capsules to evade host immune mechanisms and proliferate within the host. However, there has been a rise in detection of carbapenemase genes carried in hvkp<sup>5,6</sup>. I hypothesize that hvkp strains of *K. pneumoniae* containing carbapenemase encoded on plasmids likely have higher mutations and genetic variants that affect capsule genes, such as *rmpA* and *rmpA2*, that contributes to a less effective capsule the intake of carbapenemase resistance encoded plasmids.

## The steps for this pipeline are:

1. Download reference genome and reads <b>SRA_toolkit</b>
2. Align reads to the reference genome <b>bwa mem</b>
3. Call variants and manipulate <b>bcftools</b>
4. Gene annotation <b>snpEff</b>


## Directed Acyclic Graph:

![image](https://user-images.githubusercontent.com/83785437/144008656-4c6c9095-77c9-416e-8b81-122b0311f250.png)

## Heres how to access the git repository:

Cloning the repository:

Create folder where you want the repo

Open terminal in that folder

In terminal enter:
<br>```git clone https://github.com/kluongni/MBB659Termproject.git```

Change directory to workflow with:
<br>```cd /MBB659Termproject/workflow```

Assuming the user has conda installed:
<br>if not: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

Activate the conda environment with:
<br>```conda env create --file environment.yml```
<br>(press y when prompted)
<br>```conda activate termProject```
  
Run the Snakemake file within the directory:


```snakemake --cores * "results/annotatedVcf.vcf" will bring you to the end of the pipeline```
<br>\*designates amount of cores user would like to dedicate for the run.  

| Inputs:                                                                                                |
|:--------------------------------------------------------------------------------------------------------|
| GCA_000009885.1_ASM988v1 is a hvkp whole-genome assembly used as a reference genome for alignment.     | 
| SRR10160941 is the SRA accession for a Illumina High-throughput sequenced carbapenemase carrying hvkp. | 

| Outputs:                                                                                              | 
|:-------------------------------------------------------------------------------------------------------|
| snpEff_genes.txt is a text file containing the gene annotation.                                       | 
| annotatedVcf.vcf is a annotated vcf file of all the genes found within the sequence that was aligned. |


|The snpEFF_genes.txt provides valuable information on the genes returned from the annotation. The upstream and downstream genetic variants can be parsed from the file to provide further analyses. On the right, the graph shows that contrary to my hypothesis, there were no significant amount of genetic variations that had a detrimental effect in the rmpA gene that I believed would lead to carbapenemase acquisition. | ![image](https://user-images.githubusercontent.com/83785437/144008573-c04a5939-cf96-4e3e-8569-6341368b8465.png) |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|



References:
1.	Navon-Venezia, S., Kondratyeva, K. & Carattoli, A. Klebsiella pneumoniae: a major worldwide source and shuttle for antibiotic resistance. FEMS Microbiol. Rev. 013, 252–275 (2017).
2.	Sands, K. et al. Characterization of antimicrobial-resistant Gram-negative bacteria that cause neonatal sepsis in seven low- and middle-income countries. Nat. Microbiol. 23, 24.
3.	Wyres, K. L. & Holt, K. E. Klebsiella pneumoniae as a key trafficker of drug resistance genes from environmental to clinically important bacteria. Curr. Opin. Microbiol. 45, 131–139 (2018).
4.	Chiu, S. K. et al. Carbapenem Nonsusceptible Klebsiella pneumoniae in Taiwan: Dissemination and Increasing Resistance of Carbapenemase Producers During 2012-2015. Sci. Rep. 8, 1–9 (2018).
5.	Lee, C. R. et al. Antimicrobial resistance of hypervirulent Klebsiella pneumoniae: Epidemiology, hypervirulence-associated determinants, and resistance mechanisms. Front. Cell. Infect. Microbiol. 7, (2017).
6.	Xie, M. et al. Clinical evolution of ST11 carbapenem resistant and hypervirulent Klebsiella pneumoniae. Commun. Biol. 4, 1–9 (2021).

