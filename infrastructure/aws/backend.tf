# Backend configuration require a AWS storage bucket.
terraform {
  backend "s3" {
    bucket = "datalake-enem2020-vinisiq"
    key    = "state/terraform.tfstate"
    region = "us-east-1"
  }
}
