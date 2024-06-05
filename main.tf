provider "aws" {
  region = "ap-south-1"
}

# Conditional S3 bucket resource
resource "aws_s3_bucket" "b" {
  count  = var.bucket_name != "" ? 1 : 0
  bucket = var.bucket_name
}

# Conditional EC2 instance resource
resource "aws_instance" "web" {
  count         = var.instance_type != "" ? 1 : 0
  ami           = var.ami
  instance_type = var.instance_type

  tags = {
    Name = var.instance_name
  }

  root_block_device {
    volume_size = var.storage
  }
}
