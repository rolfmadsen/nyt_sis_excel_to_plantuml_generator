# Nyt SIS Informationsmodel UML Diagram Generator

Nyt SIS is a program to implement a new Student Information System at most of the danish universities.

Sparx Enterprise Architect is used to model the project information model and the diagrams and Excel data is exported and published at https://informationsmodeller.sdu.dk/sis/.

This repository provides a script to generate a PlantUML class diagram from the structured Excel file export.
The diagram is generated using PlantUML syntax, allowing for the visualization of complex relationships between classes, attributes, and enumerations in a consistent and organized manner.

## Features

- **Class Diagram Generation**: Automatically generate UML class diagrams based on the data provided in the Excel sheets. The script processes classes, attributes, relationships, and enumerations, formatting them according to the PlantUML syntax.
- **Support for Stereotypes and Cardinality**: Attributes with specific stereotypes (e.g., `BK`) are grouped and formatted accordingly. Cardinalities and data types are also handled correctly.
- **Abstract Classes**: Classes marked as abstract in the Excel sheet are correctly represented in the UML diagram.
- **Dynamic Relationships**: Relationships between classes are labeled and directed based on the information provided in the Excel sheet.

## Setup

### 1. Setting Up a Virtual Environment

Start by creating a virtual environment for your project. This isolates your project dependencies from your global Python installation.

```bash
# Navigate to your project directory
cd /path/to/your/project

# Create a virtual environment named 'venv'
python3 -m venv venv
```

### 2. Activating the Virtual Environment

Activate the virtual environment. The command to activate the virtual environment differs depending on your operating system:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

After you're done working in your virtual environment, you can deactivate it:

```bash
deactivate
```

### 3. Download the PlantUML generator

Make sure Jave is already installed!

Download the GPL v2 version of the compiled jar PlantUML generator from [https://plantuml.com](https://plantuml.com/download)/ to the script folder

### 4. Install required Python Packages

Use the following command to install dependencies:

```bash
pip install -r requirements.txt
```

### 5. Freeze New Packages

If you install additional Python packages, you can freeze them into your `requirements.txt` file by running:

```bash
pip freeze > requirements.txt
```

This will update the `requirements.txt` file with the latest versions of all installed packages, ensuring consistency across different environments.

## Usage

### 1. Generate UML Class Diagram

To generate the UML diagram from the Excel file, run the following command:

```bash
python3 main.py
```

This will produce a `sis_informationmodel.puml` file containing the PlantUML code for your class diagram.

### 2. Generate Diagram Images

After generating the `sis_informationmodel.puml` file, you can create different image formats of the diagram using PlantUML. 

#### 4. Running a PicoWeb Server:

To run a local web server that allows you to view the UML diagrams in your browser, use the following command:

```bash
java -jar plantuml-gplv2-1.2024.4.jar -picoweb
```

This will start a PicoWeb server on your machine, and you can access it by navigating to `http://localhost:8080` in your browser.

#### 5. Generate SVG Image:

To generate an SVG image of the UML diagram, run:

```bash
java -jar plantuml-gplv2-1.2024.4.jar -svg sis_informationmodel.puml -charset UTF-8
```

This will produce a high-quality SVG image of your UML diagram, encoded in UTF-8.

## Conclusion

This script automates the generation of UML class diagrams from Excel data, providing an efficient way to visualize and manage complex information models. By following the steps outlined above, you can easily create, view, and export your UML diagrams in various formats.
