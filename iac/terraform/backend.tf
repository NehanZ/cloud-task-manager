terraform {
  backend "s3" {
    bucket         = "task-manager-tf-state"
    key            = "global/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "task-manager-terraform-locks"
  }
}
