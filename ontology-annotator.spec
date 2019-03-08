/*
A KBase module: ontology-annotator
*/

module ontology-annotator {
    typedef structure {
		string workspace_id;
		string workspace_name;
		int cols;
		int rows;
	} ontologyInput;
	
	typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_ontology-annotator(ontologyInput params) returns (ReportResults output) authentication required;

};
