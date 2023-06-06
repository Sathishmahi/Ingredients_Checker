echo "START CREATE ENV"
conda create -p venv python=3.10 -y
echo "CONDA ENV CREATE DONE"
source activate venv/
echo "INSTALL REQUIREMENTS TXT"
pip install -r requirements.txt
echo "REQUIREMENTS TXT INSTALL DONE"