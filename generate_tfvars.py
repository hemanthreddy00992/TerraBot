with open('bucket_name.txt', 'r') as file:
    bucket_name = file.read().strip()

with open('terraform.tfvars', 'w') as file:
    file.write(f'bucket_name = "{bucket_name}"\n')

