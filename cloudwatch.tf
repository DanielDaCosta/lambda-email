resource "aws_cloudwatch_log_group" "log_lambda" {
  name              = "/aws/lambda/${local.name_dash}-${var.lambda_name}"
}