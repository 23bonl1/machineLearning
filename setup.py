from setuptools import setup, find_packages

def parse_requirements(file_name):
    """Reads a requirements.txt file and returns a list of dependencies."""
    with open(file_name, 'r') as f:
        # Using list() to create a list of non-empty, non-comment lines
        return list(
            line.strip() for line in f.readlines() if line.strip() and not line.startswith("#")
        )  
    

setup(
    name="machineLearning",  # Replace with your project's name
    version="0.1",  # Initial version
    packages=find_packages(),  # Automatically find all packages in the current directory
    install_requires=parse_requirements('requirements.txt'),
    author="Bose",  # Add your name or organization
    description="Machine Learning project",
    long_description=open('README.md').read(),  # If you have a README.md file
    long_description_content_type='text/markdown'
)