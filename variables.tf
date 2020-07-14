variable "environment" {
  description = "Env"
}

variable "name" {
  description = "Application Name"
  type        = string
}

locals {
  name_dash = "${var.name}-${var.environment}"
}

variable "region" {
  description = "AWS region for policies"
  type        = string
  default     = "us-east-1"
}

variable "lambda_name" {
  description = "Lambda Function Name"
  type        = string
}

# Credentials
variable "EMAIL_ADDRESS" {
  description = "Email to send from"
  type        = string
}
variable "EMAIL_PASS" {
  description = "Email password for smtplib email"
  type        = string
}
variable "SENDGRID_API_KEY" {
  description = "Sendgrid API Key"
  type        = string
}