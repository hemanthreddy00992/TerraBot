from flask import Flask, request, render_template, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"
    with open('app.log', 'a') as log_file:
        log_file.write(log_message + '\n')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resource_type = request.form['resource_type']
        if resource_type == 's3':
            bucket_name = request.form['bucket_name']
            with open('bucket_name.txt', 'w') as file:
                file.write(bucket_name)
            with open('terraform.tfvars', 'w') as file:
                file.write(f'bucket_name = "{bucket_name}"\n')
                # Write default values for EC2 variables to avoid prompting
                file.write('instance_type = ""\n')
                file.write('storage = 0\n')
                file.write('ami = ""\n')
                file.write('instance_name = ""\n')
            log(f"Creating S3 bucket: {bucket_name}")
            os.system('terraform init >> app.log 2>&1')
            os.system('terraform apply -auto-approve >> app.log 2>&1')
            log("Terraform apply completed for S3")
            return render_template('index.html', message="Terraform apply completed for S3")
        elif resource_type == 'ec2':
            instance_type = request.form['instance_type']
            storage = request.form['storage']
            ami = request.form['ami']
            instance_name = request.form['instance_name']
            with open('ec2_params.txt', 'w') as file:
                file.write(f'{instance_type},{storage},{ami},{instance_name}')
            with open('terraform.tfvars', 'w') as file:
                # Write default values for S3 bucket to avoid prompting
                file.write('bucket_name = ""\n')
                # Write EC2 variable values
                file.write(f'instance_type = "{instance_type}"\n')
                file.write(f'storage = {storage}\n')
                file.write(f'ami = "{ami}"\n')
                file.write(f'instance_name = "{instance_name}"\n')
            log(f"Creating EC2 instance: {instance_name} (Type: {instance_type}, Storage: {storage}GB, AMI: {ami})")
            os.system('terraform init >> app.log 2>&1')
            os.system('terraform apply -auto-approve >> app.log 2>&1')
            log("Terraform apply completed for EC2")
            return render_template('index.html', message="Terraform apply completed for EC2")
    return render_template('index.html')

@app.route('/logs', methods=['GET'])
def logs():
    with open('app.log', 'r') as log_file:
        return log_file.read()

if __name__ == '__main__':
    if not os.path.exists('app.log'):
        with open('app.log', 'w') as log_file:
            log_file.write('')  # Create an empty log file if it doesn't exist
    app.run(host="0.0.0.0", port=5000, debug=True)

