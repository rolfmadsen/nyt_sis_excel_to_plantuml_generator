import requests
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import polars as pl
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class RelationshipMapper:
    """Maps relationship types to PlantUML syntax."""
    REL_TYPE_MAP = {
        "Association": "--",
        "Generalization": "<|--",
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
    """Generates PlantUML code from class, relationship, and enum data."""
    
    def __init__(self, classes: dict, relationships: list, enums: dict):
        self.classes = classes
        self.relationships = relationships
        self.enums = enums
    
    def generate(self) -> str:
        plantuml_code = """
@startuml Nyt SIS Informationsmodel
Title Nyt SIS Informationsmodel
hide empty members
skinparam class {
    BackgroundColor<<enum>> #lightgreen
}
"""
        # Add classes and attributes
        for class_name, attrs in self.classes.items():
            plantuml_code += f"{'abstract ' if class_name.startswith('abstract ') else ''}class {class_name.replace('abstract ', '')} {{\n"
            normal_attributes, bk_attributes = self._process_attributes(attrs)
            for attr in normal_attributes:
                plantuml_code += f"  {attr}\n"
            if bk_attributes:
                plantuml_code += "  <<BK>>\n"
                for bk_attr in bk_attributes:
                    plantuml_code += f"  {bk_attr}\n"
            plantuml_code += "}\n\n"

        # Add relationships
        for rel in self.relationships:
            plantuml_code += self._generate_relationship_line(rel)

        # Add enumerations
        for enum_name, values in self.enums.items():
            plantuml_code += f"enum {enum_name} <<enum>> {{\n"
            for value in values:
                plantuml_code += f"    {value}\n"
            plantuml_code += "}\n"

        plantuml_code += "\n@enduml"
        return plantuml_code

    def _process_attributes(self, attrs: list) -> tuple:
        """Process attributes and return normal and BK attributes."""
        normal_attributes = []
        bk_attributes = []
        for attr in attrs:
            if isinstance(attr, tuple):
                attr_name, stereotype, computed, value_count, datatype = attr
                if computed == 'Ja':
                    attr_name = f"/{attr_name}"
                if datatype:
                    attr_name = f"{attr_name}: {datatype}"
                if value_count:
                    attr_name = f"{attr_name} [{value_count}]"
                if stereotype == 'BK':
                    bk_attributes.append(attr_name)
                else:
                    normal_attributes.append(attr_name)
            else:
                normal_attributes.append(attr)
        return normal_attributes, bk_attributes

    def _generate_relationship_line(self, rel: dict) -> str:
        """Generate a PlantUML relationship line."""
        source = rel['source']
        target = rel['target']
        rel_type = RelationshipMapper.map(rel.get('type', 'Association'))

        source_card = f'"{rel.get("source_card", "")}"' if rel.get('source_card', '') else ''
        target_card = f'"{rel.get("target_card", "")}"' if rel.get('target_card', '') else ''
        rel_label = rel.get('label', '')

        relationship_line = f'{source} {source_card} {rel_type} {target_card} {target}'
        if rel_label:
            relationship_line += f' : {rel_label}'
        relationship_line += '\n'
        
        return relationship_line

class ExcelDataExtractor:
    """Extracts and processes data from an Excel file."""
    
    def __init__(self, excel_data: dict):
        self.excel_data = excel_data
        self.classes = {}
        self.relationships = []
        self.enums = {}

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
        return self.classes, self.relationships, self.enums

    def _extract_classes(self, df: pl.DataFrame):
        for row in df.iter_rows(named=True):
            class_name = row['Klasse']
            if row['Abstrakt'] and row['Abstrakt'].strip().lower() == 'ja':
                class_name = f"abstract {class_name}"
            if class_name not in self.classes:
                self.classes[class_name] = []

    def _extract_attributes(self, df: pl.DataFrame):
        for row in df.iter_rows(named=True):
            class_name = row['Klasse']
            attribute_info = (
                row['Attribut'],
                row.get('Stereotype'),
                row.get('Beregnet'),
                row.get('Antal værdier'),
                row.get('Datatype')
            )
            if class_name in self.classes:
                self.classes[class_name].append(attribute_info)

    def _extract_enums(self, df: pl.DataFrame):
        for row in df.iter_rows(named=True):
            enum_name = row['Værdiliste']
            value = row['Værdi']
            if enum_name not in self.enums:
                self.enums[enum_name] = []
            self.enums[enum_name].append(value)

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

class UMLModelGenerator:
    """Orchestrates the extraction of data, processing, and UML generation."""

    BASE_URL = "https://informationsmodeller.sdu.dk/sis/"
    
    def run(self):
        try:
            excel_url = self.fetch_latest_excel_url()
            logging.info(f"Latest Excel URL: {excel_url}")

            excel_data = self.download_excel_file(excel_url)
            extractor = ExcelDataExtractor(excel_data)
            classes, relationships, enums = extractor.process()
            
            plantuml_generator = PlantUMLGenerator(classes, relationships, enums)
            plantuml_script = plantuml_generator.generate()
            
            self.save_plantuml_script(plantuml_script)

            logging.info("PlantUML file 'sis_informationmodel.puml' generated successfully.")

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
        
        sheets = ["Klasser", "Attributter", "VærdilisteVærdier", "Relationer"]
        excel_data = {}
        
        for sheet in sheets:
            excel_data[sheet] = pl.read_excel(BytesIO(response.content), sheet_name=sheet)
        
        return excel_data

    def save_plantuml_script(self, script: str):
        with open('sis_informationmodel.puml', 'w') as f:
            f.write(script)

if __name__ == "__main__":
    UMLModelGenerator().run()
