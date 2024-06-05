with open('ec2_params.txt', 'r') as file:
    params = file.read().strip().split(',')
    instance_type, storage, ami, instance_name = params

with open('terraform.tfvars', 'w') as file:
    file.write(f'instance_type = "{instance_type}"\n')
    file.write(f'storage = {storage}\n')
    file.write(f'ami = "{ami}"\n')
    file.write(f'instance_name = "{instance_name}"\n')

