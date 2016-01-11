'''
Created on Sep 08, 2014

@author: raniba
'''

import os
from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    '''
    Runs GATK IndelRealigner with an already created target file by RealignerTargetCreator
    '''
    def __init__(self, component_name='realign', component_parent_dir=None, seed_dir=None):
       self.version = "0.0.1"

        ## initialize ComponentAbstract
       super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        '''
        generates the IndelRealigner process
        '''

        java_mem = '-Xmx3072M'
        java_jar_option = '-jar'
        realign_jar = self.requirements['gatk']
        realign_infile = self.args.infile
        realign_sorted_alignment = self.args.sorted_alignment
        realign_outfile = self.args.outfile
        realign_ref_genome = self.args.ref_genome

        cmd = self.requirements['java']
        cmd_args = [
              java_mem,
              java_jar_option,
              realign_jar,
              "-T", "IndelRealigner",
              "-R", realign_ref_genome,
              "-targetIntervals", realign_infile,
              "-I", realign_sorted_alignment,
              "-o", realign_outfile
              ]

        return cmd, cmd_args


# to run as stand alone
def _main():
    '''main function'''
    realign = Component()
    realign.args = component_ui.args
    realign.run()

if __name__ == '__main__':

    import component_ui

    _main()
