# {{cookiecutter.project}}

## Installation

### Anaconda

To an existing environment:  
`$ conda install --file requirements.txt`  

Create a new environment:  
`$ conda create -n {{cookiecutter.project}} python={{cookiecutter.pythonversion}} --file requirements.txt`    
`$ conda activate {{cookiecutter.project}}`

### Virtualenv

`$ virtualenv venv_{{cookiecutter.project}}``  
`$ pip install -r requirements.txt``

