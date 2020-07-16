import json
import os
import sys
import pandas as pd
from botocore.exceptions import EndpointConnectionError


location = '.'


def join(row, students):
    """
    Performs the join operation on the teacher and student object
  
    Parameters: 
    row (dict): Teacher dictionary
    students (list): List of students dictionary
  
    Returns: 
    dict: Populated dictionary
    """
    tmp = {
        'teacher_id': row['id'],
        'teacher_name': row['fname'] + ' ' + row['lname'],
            'cid': row['cid']
    }
    tmp['students'] = []
    for _, r in students[students['cid'] == row['cid']].iterrows():
        tmp['students'].append({'student_id': r['id'], 'student_name': r['fname'] + ' ' + r['lname'] })
    return tmp


def generate_result():
    """
    Generate the solution and creates the result.json file
    Parameters: None  
    """
    teachers, students = None, None
    for file in FILES:
        if file.endswith('.parquet'):
            teachers = pd.read_parquet(
                location + '/teachers.parquet',
                                       engine='pyarrow')
        elif file.endswith('.csv'):
            students = pd.read_csv(
                location + '/students.csv', delimiter='_')
    parse_data = [join(row, students) for _, row in teachers.iterrows()]
    data = json.dumps(parse_data, indent=4)
    with open('output.json', 'w') as file:
            file.write(data)


FILES=['teachers.parquet', 'students.csv']

if __name__ == "__main__":
    try:
        local_files=os.listdir()
        print()
        print('Scanning files......')
        if FILES[0] not in local_files or FILES[1] not in local_files:
            print('.'*50)
            print(
                f'Info: {FILES[0]} or {FILES[1]} not found in your local system, please provide path of directory where {FILES[0]} and {FILES[1]} are stored.')
            print('.'*50)
            print()
            print(
                'Enter local path or s3 bucket path and hit Enter to continue or q to quit')
            path=input('> ')
            if (path.lower() == 'q'):
                print('Bye...')
                exit(0)
            else:
                if path.startswith('s3'):
                    location=path
                elif not os.path.exists(path):
                    print('Path you provide did\'t exist. Please provide path like s3://bucket_name/files_directory or /local/path/of/root/directory and please try again with proper path.')
                    exit(0)
                else:
                    location=path
        else:
            print('\nHit Enter to continue with correct directory or provide S3 path if you want to use S3')
            should_continue = input('> ')
            if should_continue:
                location = should_continue
            print()
            print('Getting things done, Please wait...')
            print()

        generate_result()

        print('Success: successfully generated the "output.json" file')
        print('Done')
    except EndpointConnectionError:
        print("Please configure your aws cli on system carefully")
