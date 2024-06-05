variable "bucket_name" {
  description = "The name of the S3 bucket"
  type        = string
}

variable "instance_type" {
  description = "The type of instance to create"
  type        = string
}

variable "storage" {
  description = "The size of the root storage volume (in GB)"
  type        = number
}

variable "ami" {
  description = "The AMI ID to use for the instance"
  type        = string
}

variable "instance_name" {
  description = "The name to assign to the instance"
  type        = string
}

