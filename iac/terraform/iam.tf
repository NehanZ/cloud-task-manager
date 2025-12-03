resource "aws_iam_user" "deployer" {
  name = var.user_name
}

# we will restrict later
resource "aws_iam_user_policy_attachment" "admin_access" {
  user       = aws_iam_user.deployer.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}


/*
resource "aws_iam_access_key" "deployer_key" {
    user = aws_iam_user.deployer.name
}

output "access_key_id" {
    value = aws_iam_access_key.deployer_key.id
}

output "secret_access_key" {
    value     = aws_iam_access_key.deployer_key.secret
    sensitive = true
}
*/
