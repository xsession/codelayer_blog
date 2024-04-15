import sys
print(sys.executable)
import os
import shutil
from pathlib import Path
import subprocess
import socket
import requests

def is_connected():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return True if response.status_code == 200 else False
    except requests.ConnectionError:
        return False

def install_dependencies_and_restart():
    if is_connected():
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "../requirements.txt"])
        except Exception as e:
            print(f"Failed to install dependencies. Error: {e}")
    else:
        print("No internet connection available. Please check your connection.")

def check_dependencies():
    with open('../requirements.txt', 'r') as f:
        packages = f.readlines()

    for package in packages:
        package_name = package.split('==')[0]
        try:
            __import__(package_name)
        except ImportError:
            install_dependencies_and_restart()
            break

check_dependencies()

def is_miktex_installed():
    try:
        subprocess.run(['pdflatex', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_miktex():
    try:
        subprocess.run(['choco', 'install', 'miktex'], check=True)
        print("MiKTeX installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install MiKTeX.")

if not is_miktex_installed():
    install_miktex()


if not is_miktex_installed():
    print("MiKTeX is not installed.")
    install_miktex()
else:
    print("MiKTeX is already installed.")


def is_graphviz_installed():
    try:
        subprocess.run(['dot', '-V'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_graphviz():
    try:
        subprocess.run(['choco', 'install', 'graphviz'], check=True)
        print("Graphviz installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install Graphviz.")

if not is_graphviz_installed():
    install_graphviz()


if not is_graphviz_installed():
    print("Graphviz is not installed.")
    install_graphviz()
else:
    print("Graphviz is already installed.")

from wireviz import wireviz

# Get the absolute path of the directory containing conf.py
dir_path = Path(__file__).parent.absolute()

# Combine this with the relative path to get the absolute path to plantuml.jar
plantuml_jar_path = dir_path / 'plantuml.jar'

plantuml = f'java -jar {plantuml_jar_path}'

cabling_file_path = Path(dir_path / '_static' / 'cabling').absolute() 
print(cabling_file_path)
cabling_output_path = Path(dir_path / '_static' / 'cabling' / 'output').absolute() 
print(cabling_output_path)
wireviz.parse_file(cabling_file_path / 'cabling.yml', cabling_output_path / 'cabling')



# Rest of your application code


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'code_layer_blog'
copyright = '2024, CodeLayer company'
author = 'Laszlo Ivanyi'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['m2r',
              'sphinx_rtd_dark_mode',
              'sphinxcontrib.plantuml',
              'sphinxcontrib.datatemplates',
              'sphinx_simplepdf',
              'sphinxcontrib.drawio']

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'web/decorator.css',
]
html_js_files = [
    
]
html_output_folder = '.'
# html_logo = '_static/connection.png'

latex_documents = [
  ('index', 'code_layer_blog.tex', u'code_layer_blog',
   u'Laszlo Ivanyi', 'manual'),
]