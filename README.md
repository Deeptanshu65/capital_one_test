## **Task :**
The goal of this project is to create a small app in python, An application that processes the two data files [students.csv , teachers.parquet]. The application should use both files to output a report in json listing each student and the teacher.
The application will be used with both local and files stored in aws S3, so there should be an easy way to specify the location of these files and the output json.
 

### System requirements
- OpenSSL 1.1.1
- python 3.5
 

### Dependencies
- botocore==1.17.16
- pandas==1.0.5
- pyarrow==0.17.1
 

### Environment Setup

Clone the repository
```bash
git clone https://github.com/Deeptanshu65/capital_one_test.git
cd capital_one_test
```

To create a virtual environment
```bash
python -m virtualenv env
```

Activate the environment
```bash
source env/bin/activate
```

Install requirements
```bash
pip install -r requirements.txt
```

### Run
```bash
python3 solution.py
# and follow the instructions
```

### Docker commands
```bash
docker build -t <username>/test_data:latest .
docker run -it <username>/test_data
```
