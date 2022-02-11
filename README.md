# KoboAnnotations
Tiny Python script that parses a KoboReader.sqlite file and outputs all annotations in a HTML file.

# Requeriments
* Jinja2

# Install
Clone this repository and run
`pip install .`
Pip will read the pyproject file and import the dependencies.

# Usage
### Windows
Drop your .sqlite file on KoboAnnotations.py
### Linux
Navigate to `src/KoboAnnotations`, paste your KoboReader.sqlite file in this folder, and run `python KoboAnnotation.py KoboReader.sqlite`

# Note
This app has only been tested with a Kobo Aura H2O edition 2 with the latest firmware at the time of writing, 4.28.18220. I can't promise
it will work correctly with other models or versions of firmware.

