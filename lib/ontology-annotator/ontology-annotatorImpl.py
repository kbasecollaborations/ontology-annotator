# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
import shutuil

from installed_clients.KBaseReportClient import KBaseReport
#END_HEADER


class ontology-annotator:
    '''
    Module Name:
    ontology-annotator

    Module Description:
    A KBase module: ontology-annotator
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def run_ontology-annotator(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of type "ontologyInput" -> structure:
           parameter "workspace_id" of String, parameter "workspace_name" of
           String, parameter "cols" of Long, parameter "rows" of Long
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_ontology-annotator
        report = KBaseReport(self.callback_url)

        hmtl_src = "/kb/module/report"
        html_dest = self.shared_folder

        shutil.copytree(html_src, html_dest)

        html_file = {
            'path': os.path.join(self.shared_folder, 'report'),
            'name': 'ontology.html',  # MUST match the filename of your main html page
            'description': 'My HTML report'
        }

        report_info = report_client.create_extended_report({
            'direct_html_link_index': 0,
            'html_links': [html_file],
            'report_object_name': report_name,
            'workspace_name': workspace_name
        })

        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }
        #END run_ontology-annotator

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_ontology-annotator return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
