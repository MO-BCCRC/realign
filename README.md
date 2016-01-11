#realign: Emits intervals for the Local Indel Realigner to target for realignment.


```
Development information

date created : Sep 08 2014
last update  : Sep 08  2014
Developer    : Rad Aniba (raniba@bccrc.ca)
Input        : Target file, sorted alignment, reference genome
Output       : Bam file
Seed used    : <no_seed>

```


###Usage

The local realignment tool is designed to consume one or more BAM files and to locally realign reads such that the number of mismatching bases is minimized across all the reads. In general, a large percent of regions requiring local realignment are due to the presence of an insertion or deletion (indels) in the individual's genome with respect to the reference genome. Such alignment artifacts result in many bases mismatching the reference near the misalignment, which are easily mistaken as SNPs. Moreover, since read mapping algorithms operate on each read independently, it is impossible to place reads on the reference genome such that mismatches are minimized across all reads. Consequently, even when some reads are correctly mapped with indels, reads covering the indel near just the start or end of the read are often incorrectly mapped with respect the true indel, also requiring realignment. Local realignment serves to transform regions with misalignments due to indels into clean reads containing a consensus indel suitable for standard variant discovery approaches. Unlike most mappers, this walker uses the full alignment context to determine whether an appropriate alternate reference (i.e. indel) exists. Following local realignment, the GATK tool Unified Genotyper can be used to sensitively and specifically identify indels.

There are 2 steps to the realignment process:  
1- Determining (small) suspicious intervals which are likely in need of realignment (RealignerTargetCreator)  
2- Running the realigner over those intervals (see the IndelRealigner tool)
Important note 1: the input BAM(s), reference, and known indel file(s) should be the same ones to be used for the IndelRealigner step.

Important note 2: when multiple potential indels are found by the tool in the same general region, the tool will choose the most likely one for realignment to the exclusion of the others. This is a known limitation of the tool.

Important note 3: because reads produced from the 454 technology inherently contain false indels, the realigner will not currently work with them (or with reads from similar technologies). This tool also ignores MQ0 reads and reads with consecutive indel operators in the CIGAR string.

###Dependencies

- GATK
- python



###Example

(will update later)

###Known issues

(will update later)

###Last updates

(will update later)

### test data
Reference : /genesis/extscratch/shahlab/raniba/Software/bowtie2/genomes/GRCh37-lite   
seq1 : /extscratch/shahlab/raniba/Tasks/test_data/SA495-Normal_S8_L001_R1_001.fastq 
seq2 : /extscratch/shahlab/raniba/Tasks/test_data/SA495-Normal_S8_L001_R2_001.fastq  
outfile : test.bam   

bowtie2 path : /genesis/extscratch/shahlab/raniba/Software/bowtie2/  
samtools path : /extscratch/shahlab/raniba/pipelines/miseq_pipeline/miseq_analysis_pipeline/miseq-pipeline/software/samtools-0.1.19/samtools 


