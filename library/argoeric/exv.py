import os
import time
from datetime import datetime

import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

import argopy
from argopy import DataFetcher
from SPARQLWrapper import SPARQLWrapper, JSON


# Access from an EXV parameter - ADDITION FROM EHN HACKATHON - APRIL 2025
# =====

def iadopt(exv_code):
    # SPARQL endpoint
    endpoint_url = "https://vocab.nerc.ac.uk/sparql/"

    # Construct full identifier
    exv_identifier = f"SDN:EXV::{exv_code}"

    # Create the query with the user input
    query = f"""
    PREFIX owl:    <http://www.w3.org/2002/07/owl#>
    PREFIX dce:    <http://purl.org/dc/elements/1.1/>
    PREFIX skos:   <http://www.w3.org/2004/02/skos/core#>
    PREFIX iadopt: <https://w3id.org/iadopt/ont#> 
    PREFIX rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT DISTINCT ?r03 ?prefLabel ?notation
    
    WHERE {{
        ?exv a skos:Concept .
        ?exv dce:identifier "{exv_identifier}" .
      
        OPTIONAL {{?exv iadopt:hasApplicableMatrix ?matrix .}}
        ?exv iadopt:hasApplicableObjectOfInterest ?ooi .
        ?exv iadopt:hasApplicableProperty ?property .
        
        <http://vocab.nerc.ac.uk/collection/P01/current/> skos:member ?p01 .
        
        OPTIONAL {{ ?p01 iadopt:hasMatrix ?matrix . }}
        ?p01 iadopt:hasObjectOfInterest ?ooi .
        ?p01 iadopt:hasProperty ?property .
        
        <http://vocab.nerc.ac.uk/collection/R03/current/> skos:member ?r03 .
        
        ?r03 owl:sameAs ?p01
        
        OPTIONAL {{ ?r03 skos:prefLabel ?prefLabel . }}
        OPTIONAL {{ ?r03 skos:notation ?notation . }}
    
    }}
    """

    # Set up the SPARQL request
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    # Run the query and parse results
    results = sparql.query().convert()

    codes = []

    # Show results
    for result in results["results"]["bindings"]:
        uri = result.get("r03", {}).get("value", "")
        codes.append(uri.rstrip("/").split("/")[-1])

    return codes
