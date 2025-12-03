resource "aws_ecr_repository" "task_manager_backend" {
  name = "task-manager-backend"

  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Project     = "task-manager"
    Environment = "prod"
    Service     = "backend"
  }
}

output "backend_ecr_repository_url" {
  value = aws_ecr_repository.task_manager_backend.repository_url
}