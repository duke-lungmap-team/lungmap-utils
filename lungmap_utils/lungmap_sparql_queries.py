
GET_BASIC_EXPERIMENTS = """
PREFIX lm: <http://www.lungmap.net/ontologies/data#>
PREFIX lmdb:<http://www.lungmap.net/ontologies/database#>
SELECT ?experiment_id ?species ?stage_label
WHERE {
    VALUES ?exp_type_id { lm:LMXT0000000003 } .
    ?experiment_id lmdb:is_experiment_type ?exp_type_id .
    ?experiment_id lmdb:in_organism ?tax_id .
    ?tax_id rdfs:label ?species . 
    ?experiment_id lmdb:uses_sample ?sample_id . 
    ?sample_id lmdb:in_stage ?stage .
    ?stage rdfs:label ?stage_label .
}
"""

GET_IMAGES_BY_EXPERIMENT = """
PREFIX lm: <http://www.lungmap.net/ontologies/data#>
PREFIX lmdb: <http://www.lungmap.net/ontologies/database#>
SELECT DISTINCT strafter(str(?experiment),'#') as ?experiment strafter(str(?experiment_type),'#') as ?experiment_type ?image ?path ?dir ?magnification ?x_scaling ?y_scaling ?image_file_path
WHERE {
    VALUES ?experiment { lm:EXPERIMENT_PLACEHOLDER } .
    ?image lmdb:part_of_experiment ?experiment .
    ?image lmdb:directory ?dir .
    ?image lmdb:magnification ?magnification .
    ?image lmdb:x_scaling ?x_scaling .
    ?image lmdb:y_scaling ?y_scaling .
    ?image lmdb:has_supporting_file ?image_file_id .
    ?image_file_id lmdb:display_url ?image_file_path .
    ?experiment lmdb:s3_path ?path .
    ?experiment lmdb:is_experiment_type ?experiment_type
} ORDER BY ASC(xsd:integer(REPLACE(str(?magnification), 'X', '')))
"""


GET_PROBE_BY_EXPERIMENT = """
PREFIX lm: <http://www.lungmap.net/ontologies/data#>
PREFIX lmdb: <http://www.lungmap.net/ontologies/database#>
SELECT DISTINCT ?experiment_id ?probe_id ?probe_label ?color
WHERE {
    VALUES ?experiment_id { lm:EXPERIMENT_PLACEHOLDER } .
    ?image lmdb:part_of_experiment ?experiment_id .
    ?image lmdb:has_probe_color ?probe_color .
    ?probe_color lmdb:maps_to ?probe_id .
    ?probe_color lmdb:color ?color .
    ?probe_id rdfs:label ?probe_label
}
"""


GET_PROBES = """
PREFIX lmdata: <http://www.lungmap.net/ontologies/data#>
PREFIX lmdb: <http://www.lungmap.net/ontologies/database#>
SELECT DISTINCT ?probe_label
WHERE {
  ?probe_id a lmdb:probe .
  ?probe_id rdfs:label ?probe_label .
  ?probe_id lmdb:probe_type lmdata:antibody_probe .  
} order by ?probe_label
"""


GET_MAGNIFICATIONS = """
PREFIX lmdata: <http://www.lungmap.net/ontologies/data#>
PREFIX lmdb: <http://www.lungmap.net/ontologies/database#>
SELECT DISTINCT ?o
WHERE {
  ?s lmdb:magnification ?o .
} order by ?o
"""

GET_IMAGES_BY_METADATA = """
PREFIX lmdata: <http://www.lungmap.net/ontologies/data#>
PREFIX lmdb: <http://www.lungmap.net/ontologies/database#>
SELECT DISTINCT ?exp ?stage_label ?mag ?probe1 ?color1 ?probe2 ?color2 ?probe3 ?color3 ?image ?image_url
WHERE {
  VALUES(?probe1) {("PROBE1_PLACEHOLDER")} .
  VALUES(?probe2) {("PROBE2_PLACEHOLDER")} .
  VALUES(?probe3) {("PROBE3_PLACEHOLDER")} .
  VALUES(?mag) {("MAG_PLACEHOLDER")} .
  VALUES(?stage_label) {("STAGE_PLACEHOLDER")} .
  ?exp a lmdb:experiment .
  ?exp lmdb:in_stage ?stage .
  ?stage rdfs:label ?stage_label .
  ?exp lmdb:has_probe_color ?probe1_color .
  ?exp lmdb:has_probe_color ?probe2_color .
  ?exp lmdb:has_probe_color ?probe3_color .
  ?probe1_color lmdb:maps_to ?probe1_id .
  ?probe2_color lmdb:maps_to ?probe2_id .
  ?probe3_color lmdb:maps_to ?probe3_id .
  ?probe1_color lmdb:color ?color1 .
  ?probe2_color lmdb:color ?color2 .
  ?probe3_color lmdb:color ?color3 .
  ?probe1_id rdfs:label ?probe1 .
  ?probe2_id rdfs:label ?probe2 .
  ?probe3_id rdfs:label ?probe3 .
  ?image lmdb:part_of_experiment ?exp .
  ?image rdf:type lmdb:expression_image .
  ?image lmdb:magnification ?mag .
  ?image lmdb:has_supporting_file ?image_file .
  ?image_file lmdb:file_type "image_original" .
  ?image_file lmdb:display_url ?image_url
} ORDER BY ?exp
"""
