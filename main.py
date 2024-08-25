import requests
import pandas as pd
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to map relationship types to PlantUML syntax
def map_relationship_type(rel_type):
    mapping = {
        "Association": "--",
        "Generalization": "<|--",
        "Dependency": ".right.>",
        "Aggregation": "o--",
        "Composition": "*--",
        "Realization": "<|.."
    }
    return mapping.get(rel_type, "--")  # Default to association if no match found

# Function to generate the PlantUML content with proper relationships and cardinalities
def generate_plantuml(classes, relationships, enums):
    plantuml_code = """
@startuml Nyt SIS Informationsmodel
Title Nyt SIS Informationsmodel
hide empty members
skinparam class {
    BackgroundColor<<enum>> #lightgreen
}
"""

    # Define classes and their attributes
    for class_name, attrs in classes.items():
        if class_name.startswith("abstract "):
            plantuml_code += f"abstract {class_name.replace('abstract ', '')} {{\n"
        else:
            plantuml_code += f"class {class_name} {{\n"
        
        # Separate attributes based on the 'BK' stereotype
        normal_attributes = []
        bk_attributes = []
        
        for attr in attrs:
            if isinstance(attr, tuple):  # If the attribute is a tuple with extra info
                attr_name, stereotype, computed, value_count, datatype = attr
                
                # Add '/' if Beregnet is "Ja"
                if computed == 'Ja':
                    attr_name = f"/{attr_name}"
                
                # Append Datatype if available
                if pd.notna(datatype) and datatype != "":
                    attr_name = f"{attr_name}: {datatype}"
                
                # Append value of Antal værdier if available
                if pd.notna(value_count) and value_count != "":
                    attr_name = f"{attr_name} [{value_count}]"
                
                if stereotype == 'BK':
                    bk_attributes.append(attr_name)
                else:
                    normal_attributes.append(attr_name)
            else:
                normal_attributes.append(attr)

        # Add normal attributes first
        for attr in normal_attributes:
            plantuml_code += f"  {attr}\n"
        
        # If there are BK attributes, add <<BK>> and then list them
        if bk_attributes:
            plantuml_code += "  <<BK>>\n"
            for bk_attr in bk_attributes:
                plantuml_code += f"  {bk_attr}\n"
        
        plantuml_code += "}\n\n"

    # Define relationships with cardinality and correct type
    for rel in relationships:
        source = rel['source']
        target = rel['target']
        rel_type = map_relationship_type(rel.get('type', 'Association'))

        # Handle cardinalities
        source_card = rel.get('source_card', '')
        target_card = rel.get('target_card', '')
        rel_label = rel.get('label', '')

        # Only include cardinality if it's not NaN or empty
        source_card = f'"{source_card}"' if pd.notna(source_card) and source_card else ''
        target_card = f'"{target_card}"' if pd.notna(target_card) and target_card else ''
        
        # Construct the relationship line without empty quotes and with label if present
        relationship_line = f'{source} {source_card} {rel_type} {target_card} {target}'
        if rel_label and pd.notna(rel_label):
            relationship_line += f' : {rel_label}'
        relationship_line += '\n'
        plantuml_code += relationship_line

    # Add enumerations
    for enum_name, values in enums.items():
        plantuml_code += f"enum {enum_name} <<enum>> {{\n"
        for value in values:
            plantuml_code += f"    {value}\n"
        plantuml_code += "}\n"

    plantuml_code += "\n@enduml"
    return plantuml_code

# Step 1: Fetch the URL of the latest Excel file from the webpage
base_url = "https://informationsmodeller.sdu.dk/sis/"
response = requests.get(base_url)

if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first Excel file link, assuming it's the latest
    excel_link = soup.find('a', href=lambda href: href and href.endswith('.xlsx'))

    if (excel_link):
        # Resolve the relative URL to an absolute URL
        excel_url = urljoin(base_url, excel_link['href'])
        print("Latest Excel URL:", excel_url)

        # Step 2: Download the Excel file
        response = requests.get(excel_url)

        if response.status_code == 200:
            # Load the Excel file into a pandas DataFrame
            excel_data = pd.read_excel(BytesIO(response.content), sheet_name=None)

            # Initialize dictionaries to hold the extracted data
            classes = {}
            relationships = []
            enums = {}

            # Step 3: Process each sheet to extract UML information
            for sheet_name, df in excel_data.items():
                print(f"Processing sheet: {sheet_name}")
                print(df.columns)  # Print columns for debugging

                # Extract classes and attributes from the "Klasser" and "Attributter" sheets
                if sheet_name == 'Klasser':
                    for _, row in df.iterrows():
                        class_name = row['Klasse']
                        if pd.notna(row['Abstrakt']) and row['Abstrakt'].strip().lower() == 'ja':
                            class_name = f"abstract {class_name}"
                        if class_name not in classes:
                            classes[class_name] = []

                if sheet_name == 'Attributter':
                    for _, row in df.iterrows():
                        class_name = row['Klasse']
                        attribute = row['Attribut']
                        stereotype = row.get('Stereotype')
                        computed = row.get('Beregnet')
                        value_count = row.get('Antal værdier')
                        datatype = row.get('Datatype')
                        attribute_info = (attribute, stereotype, computed, value_count, datatype)
                        if class_name in classes:
                            classes[class_name].append(attribute_info)

                if sheet_name == 'VærdilisteVærdier':
                    for _, row in df.iterrows():
                        enum_name = row['Værdiliste']
                        value = row['Værdi']
                        if enum_name not in enums:
                            enums[enum_name] = []
                        enums[enum_name].append(value)

                # Extract relationships from the "Relationer" sheet
                if sheet_name == 'Relationer':
                    for _, row in df.iterrows():
                        relationships.append({
                            'source': row['Klasse1'],
                            'target': row['Klasse2'],
                            'type': row.get('Type', 'Association'),  # Default to 'Association' if no type provided
                            'source_card': row.get('Kardinalitet1', ''),
                            'target_card': row.get('Kardinalitet2', ''),
                            'label': row.get('Relation')
                        })

            # Step 4: Generate the PlantUML script with relationships and cardinality
            plantuml_script = generate_plantuml(classes, relationships, enums)

            # Step 5: Save the PlantUML script to a file
            with open('sis_informationmodel.puml', 'w') as f:
                f.write(plantuml_script)

            print("PlantUML file 'uml_diagram.puml' generated successfully.")
        else:
            print(f"Failed to download the Excel file. Status code: {response.status_code}")
    else:
        print("No Excel file link found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
