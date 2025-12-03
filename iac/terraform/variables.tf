variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  default = "task-manager"
}

variable "user_name" {
  description = "IAM user for deployment"
  type        = string
  default     = "task-manager-deployer"
}
