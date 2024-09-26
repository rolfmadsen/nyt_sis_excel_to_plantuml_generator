import requests
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import polars as pl
import logging
import os
import subprocess

# Configure logging
logging.basicConfig(level=logging.INFO)

class RelationshipMapper:
    """Maps relationship types to PlantUML syntax."""
    REL_TYPE_MAP = {
        "Association": "--",
        "Generalization": "--|>",
        "Dependency": ".right.>",
        "Aggregation": "o--",
        "Composition": "*--",
        "Realization": "<|.."
    }

    @classmethod
    def map(cls, rel_type: str) -> str:
        if rel_type not in cls.REL_TYPE_MAP:
            logging.warning(f"Unknown relationship type: {rel_type}. Defaulting to '--'.")
        return cls.REL_TYPE_MAP.get(rel_type, "--")

class PlantUMLGenerator:
    """Generates PlantUML code for each Pakke, including its classes, relationships, and enums."""

    def __init__(self, classes_by_pakke: dict, relationships: list, enums_by_pakke: dict):
        self.classes_by_pakke = classes_by_pakke
        self.relationships = relationships
        self.enums_by_pakke = enums_by_pakke

    def generate_all(self) -> dict:
        """Generates PlantUML scripts for all pakkes and a main diagram."""
        plantuml_scripts = {}
        main_code = self._generate_main_diagram()  # Generate the main diagram code

        # Save the main diagram
        plantuml_scripts['main'] = main_code

        # Generate individual Pakke files using `includesub`
        for pakke_name in self.classes_by_pakke.keys():
            sanitized_pakke_name = self._sanitize_filename(pakke_name)
            subpart_code = self._generate_individual_pakke(sanitized_pakke_name)
            plantuml_scripts[sanitized_pakke_name] = subpart_code

        return plantuml_scripts

    def _sanitize_filename(self, name: str) -> str:
        """Sanitize the Pakke name to be filesystem-friendly and replace æ, ø, å."""
        replacements = {'æ': 'ae', 'ø': 'oe', 'å': 'aa',
                        'Æ': 'Ae', 'Ø': 'Oe', 'Å': 'Aa'}
        sanitized_name = ''.join(replacements.get(c, c) for c in name)
        return "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in sanitized_name).replace(' ', '_')

    def _generate_main_diagram(self) -> str:
        """Generates the main PlantUML diagram with all elements grouped by Pakke."""
        main_code = "@startuml main\n"
        main_code += "Title SIS Information Model\n"
        main_code += "hide empty members\n"
        main_code += "skinparam linetype ortho\n"
        #main_code += "skinparam linetype polyline\n"
        main_code += "skinparam class {\n"
        main_code += "    BackgroundColor<<enum>> #lightgreen\n"
        main_code += "}\n\n"

        # Generate subparts for each Pakke
        for pakke_name, classes in self.classes_by_pakke.items():
            sanitized_pakke_name = self._sanitize_filename(pakke_name)
            main_code += f"!startsub {sanitized_pakke_name}\n"
            main_code += self._generate_classes_and_enums(classes, self.enums_by_pakke.get(pakke_name, {}))
            main_code += self._generate_relationships(pakke_name, classes)  # Pass pakke_name here
            main_code += f"!endsub\n\n"

        main_code += "@enduml\n"
        return main_code

    def _generate_individual_pakke(self, pakke_name: str) -> str:
        """Generates an individual Pakke file using includesub from the main file."""
        subpart_code = f"@startuml {pakke_name}\n"
        subpart_code += f"Title {pakke_name}\n"
        subpart_code += "hide empty members\n"
        subpart_code += "skinparam linetype ortho\n"
        #subpart_code += "skinparam linetype polyline\n"
        subpart_code += "skinparam class {\n"
        subpart_code += "    BackgroundColor<<enum>> #lightgreen\n"
        subpart_code += "}\n\n"
        subpart_code += f"!includesub main.puml!{pakke_name}\n"
        subpart_code += "@enduml\n"
        return subpart_code

    def _generate_classes_and_enums(self, classes: dict, enums: dict) -> str:
        """Generates the PlantUML code for classes and enums."""
        code = ""
        for class_name, attrs in classes.items():
            if class_name.startswith("abstract "):
                code += f"abstract {class_name.replace('abstract ', '')} {{\n"
            else:
                code += f"class {class_name} {{\n"

            normal_attributes, bk_attributes = self._process_attributes(attrs)
            for attr in normal_attributes:
                code += f"  {attr}\n"
            if bk_attributes:
                code += "  <<BK>>\n"
                for bk_attr in bk_attributes:
                    code += f"  {bk_attr}\n"
            code += "}\n\n"

        # Add enums
        for enum_name, enum_values in enums.items():
            code += f"enum {enum_name} <<enum>> {{\n"
            for value in enum_values:
                code += f"  {value}\n"
            code += "}\n\n"

        return code

    def _generate_relationships(self, pakke_name: str, classes: dict) -> str:
        """Generates the PlantUML relationships code."""
        code = ""

        # Get the enums in the current Pakke
        pakke_enums = self.enums_by_pakke.get(pakke_name, {})

        # Filter relationships:
        related_rels = [
            rel for rel in self.relationships
            # 1. Both source and target are classes/abstracts in the Pakke
            if (rel['source'] in classes and rel['target'] in classes)
            # 2. Source is in the Pakke but target is not
            or (rel['source'] in classes and rel['target'] not in classes)
            # 3. Target is in the Pakke but source is not
            or (rel['source'] not in classes and rel['target'] in classes)
            # 4. The source is a class/abstract in the Pakke, and the target is an enum in the Pakke
            or (rel['source'] in classes and rel['target'] in pakke_enums)
        ]

        for rel in related_rels:
            source = rel['source']
            target = rel['target']
            rel_type = RelationshipMapper.map(rel.get('type', 'Association'))

            source_card = f'"{rel.get("source_card", "")}"' if rel.get('source_card', '') else ''
            target_card = f'"{rel.get("target_card", "")}"' if rel.get('target_card', '') else ''
            rel_label = rel.get('label', '')

            # Clean up spacing
            source_card = f" {source_card}" if source_card else ""
            target_card = f" {target_card}" if target_card else ""

            relationship_line = f'{source}{source_card} {rel_type} {target_card} {target}'
            if rel_label:
                relationship_line += f' : {rel_label}'
            relationship_line += '\n'

            code += relationship_line

        return code

    def _process_attributes(self, attrs: list) -> tuple:
        """Process attributes and return normal and BK attributes."""
        normal_attributes = []
        bk_attributes = []
        for attr in attrs:
            if isinstance(attr, tuple):
                attr_name, stereotype, computed, value_count, datatype = attr
                if computed and isinstance(computed, str) and computed.strip().lower() == 'ja':
                    attr_name = f"/{attr_name}"
                if datatype:
                    attr_name = f"{attr_name}: {datatype}"
                if value_count:
                    attr_name = f"{attr_name} [{value_count}]"
                if stereotype and stereotype.strip().upper() == 'BK':
                    bk_attributes.append(attr_name)
                else:
                    normal_attributes.append(attr_name)
            else:
                normal_attributes.append(attr)
        return normal_attributes, bk_attributes


    def _generate_relationship_line(self, rel: dict) -> str:
        source = rel['source']
        target = rel['target']
        rel_type = RelationshipMapper.map(rel.get('type', 'Association'))

        # Skip cardinality for certain relationship types
        if rel_type in ["<|--", ".right.>"]:  # Generalization and Dependency types
            source_card = ''
            target_card = ''
        else:
            source_card = f'"{rel.get("source_card", "")}"' if rel.get('source_card', '') else ''
            target_card = f'"{rel.get("target_card", "")}"' if rel.get('target_card', '') else ''
        
        rel_label = rel.get('label', '')

        # Clean up spacing
        source_card = f" {source_card}" if source_card else ""
        target_card = f" {target_card}" if target_card else ""

        relationship_line = f'{source}{source_card} {rel_type} {target_card} {target}'
        if rel_label:
            relationship_line += f' : {rel_label}'
        relationship_line += '\n'

        return relationship_line

class ExcelDataExtractor:
    """Extracts and processes data from an Excel file."""
    
    def __init__(self, excel_data: dict):
        self.excel_data = excel_data
        self.classes_by_pakke = {}
        self.relationships = []
        self.enums_by_pakke = {}

    def process(self):
        for sheet_name, df in self.excel_data.items():
            logging.info(f"Processing sheet: {sheet_name}")
            if sheet_name == 'Klasser':
                self._extract_classes(df)
            elif sheet_name == 'Attributter':
                self._extract_attributes(df)
            elif sheet_name == 'VærdilisteVærdier':
                self._extract_enums(df)
            elif sheet_name == 'Relationer':
                self._extract_relationships(df)
            elif sheet_name == 'Værdilister':
                self._extract_enum_lists(df)
        return self.classes_by_pakke, self.relationships, self.enums_by_pakke

    def _extract_classes(self, df: pl.DataFrame):
        for row in df.iter_rows(named=True):
            pakke = row['Pakke']
            class_name = row['Klasse']
            if row['Abstrakt'] and row['Abstrakt'].strip().lower() == 'ja':
                class_name = f"abstract {class_name}"
            if pakke not in self.classes_by_pakke:
                self.classes_by_pakke[pakke] = {}
            if class_name not in self.classes_by_pakke[pakke]:
                self.classes_by_pakke[pakke][class_name] = []

    def _extract_attributes(self, df: pl.DataFrame):
        for row in df.iter_rows(named=True):
            pakke = row['Pakke']
            class_name = row['Klasse']
            attribute_info = (
                row['Attribut'],
                row.get('Stereotype'),
                row.get('Beregnet'),
                row.get('Antal værdier'),
                row.get('Datatype')
            )
            if pakke in self.classes_by_pakke and class_name in self.classes_by_pakke[pakke]:
                self.classes_by_pakke[pakke][class_name].append(attribute_info)

    def _extract_enums(self, df: pl.DataFrame):
        for row in df.iter_rows(named=True):
            pakke = row['Pakke']
            enum_name = row['Værdiliste']
            value = row['Værdi']
            if pakke not in self.enums_by_pakke:
                self.enums_by_pakke[pakke] = {}
            if enum_name not in self.enums_by_pakke[pakke]:
                self.enums_by_pakke[pakke][enum_name] = []
            self.enums_by_pakke[pakke][enum_name].append(value)

    def _extract_relationships(self, df: pl.DataFrame):
        for row in df.iter_rows(named=True):
            self.relationships.append({
                'source': row['Klasse1'],
                'target': row['Klasse2'],
                'type': row.get('Type', 'Association'),
                'source_card': row.get('Kardinalitet1', ''),
                'target_card': row.get('Kardinalitet2', ''),
                'label': row.get('Relation')
            })

    def _extract_enum_lists(self, df: pl.DataFrame):
        """Extract and store enumeration lists from the 'Værdilister' sheet."""
        logging.info(f"Columns in 'Værdilister': {df.columns}")  # Debug: Print the columns
        for row in df.iter_rows(named=True):
            enum_name = row['Værdiliste']
            pakke = row['Pakke']
            if pakke not in self.enums_by_pakke:
                self.enums_by_pakke[pakke] = {}
            if enum_name not in self.enums_by_pakke[pakke]:
                self.enums_by_pakke[pakke][enum_name] = []

        logging.info(f"Processed {len(self.enums_by_pakke)} enumeration lists from 'Værdilister'.")

class UMLModelGenerator:
    """Orchestrates the extraction of data, processing, and UML generation."""

    BASE_URL = "https://informationsmodeller.sdu.dk/sis/"
    
    def run(self):
        try:
            excel_url = self.fetch_latest_excel_url()
            logging.info(f"Latest Excel URL: {excel_url}")

            excel_data = self.download_excel_file(excel_url)
            extractor = ExcelDataExtractor(excel_data)
            classes_by_pakke, relationships_by_pakke, enums_by_pakke = extractor.process()
            
            plantuml_generator = PlantUMLGenerator(classes_by_pakke, relationships_by_pakke, enums_by_pakke)
            plantuml_scripts = plantuml_generator.generate_all()  # Use generate_all to get scripts for each pakke
            
            self.save_plantuml_scripts(plantuml_scripts)
# Remove comment to print diagrams to SVG            
            self.generate_svgs(plantuml_scripts)  # Generate SVGs from the PlantUML files

            logging.info("PlantUML files generated successfully.")

        except (ConnectionError, FileNotFoundError) as e:
            logging.error(e)

    def fetch_latest_excel_url(self) -> str:
        response = requests.get(self.BASE_URL)
        if response.status_code != 200:
            raise ConnectionError(f"Failed to retrieve the page. Status code: {response.status_code}")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        excel_link = soup.find('a', href=lambda href: href and href.endswith('.xlsx'))
        if not excel_link:
            raise FileNotFoundError("No Excel file link found.")
        
        return urljoin(self.BASE_URL, excel_link['href'])

    def download_excel_file(self, url: str) -> dict:
        response = requests.get(url)
        if response.status_code != 200:
            raise ConnectionError(f"Failed to download the Excel file. Status code: {response.status_code}")
        
        sheets = ["Klasser", "Attributter", "VærdilisteVærdier", "Relationer", "Værdilister"]
        excel_data = {}
        
        for sheet in sheets:
            excel_data[sheet] = pl.read_excel(BytesIO(response.content), sheet_name=sheet)
        
        return excel_data

    def save_plantuml_scripts(self, scripts: dict):
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)

        # Save the main diagram
        main_file_path = os.path.join(output_dir, 'main.puml')
        with open(main_file_path, 'w') as f:
            f.write(scripts['main'])
        logging.info(f"Saved main PlantUML script to '{main_file_path}'")

        # Save individual Pakke diagrams
        for pakke_name, script in scripts.items():
            if pakke_name != 'main':  # Skip the main diagram as it's already saved
                pakke_file_path = os.path.join(output_dir, f"{pakke_name}.puml")
                with open(pakke_file_path, 'w') as f:
                    f.write(script)
                logging.info(f"Saved PlantUML script to '{pakke_file_path}'")

    def generate_svgs(self, scripts: dict):
        output_dir = 'output'
        plantuml_jar_path = os.path.join(os.getcwd(), 'plantuml-gplv2-1.2024.6.jar')  # Path to the jar file

        for pakke_name in scripts.keys():
            puml_file_path = os.path.join(output_dir, f"{pakke_name}.puml")
            svg_file_path = os.path.join(output_dir, f"{pakke_name}.svg")

            result = subprocess.run([
                'java', '-jar', plantuml_jar_path,
                '-tsvg', puml_file_path,
                '-charset', 'UTF-8'
            ], capture_output=True, text=True)

            if result.returncode != 0:
                logging.error(f"Error generating SVG for '{pakke_name}': {result.stderr}")
            else:
                logging.info(f"Generated SVG for '{pakke_name}' and saved to '{svg_file_path}'")

if __name__ == "__main__":
    UMLModelGenerator().run()
