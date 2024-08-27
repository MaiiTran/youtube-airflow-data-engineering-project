sudo apt-get update
sudo apt install python3-pip

sudo apt install python3.12-venv
# Change your path
python3 -m venv ~/Documents/DRAFT/DATA_ENGINEERING
# Check if 'activate' script in the 'bin' directory: 
ls ~/Documents/DRAFT/DATA_ENGINEERING/bin
# Activate the environment
source ~/Documents/DRAFT/DATA_ENGINEERING/bin/activate 

pip install pandas
pip install s3fs
pip install google-api-python-client
pip install apache-airflow 
