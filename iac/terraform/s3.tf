resource "aws_s3_bucket" "frontend" {
  bucket = "task-manager-frontend-version1"
  acl    = "public-read"

  tags = {
    Project     = "task-manager"
    Environment = "prod"
    Owner       = "nehan"
    ManagedBy   = "manual"
  }

}

# Enable static website hosting
resource "aws_s3_bucket_website_configuration" "frontend_website" {
  bucket = aws_s3_bucket.frontend.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "index.html"
  }
}

# Public read policy for the bucket
resource "aws_s3_bucket_policy" "frontend_policy" {
  bucket = aws_s3_bucket.frontend.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "PublicReadGetObject"
        Effect    = "Allow"
        Principal = "*"
        Action    = ["s3:GetObject"]
        Resource  = "${aws_s3_bucket.frontend.arn}/*"
      }
    ]
  })
}

output "frontend_bucket_name" {
  value = aws_s3_bucket.frontend.bucket
}

output "frontend_bucket_website_url" {
  value = aws_s3_bucket_website_configuration.frontend_website.website_endpoint
}
