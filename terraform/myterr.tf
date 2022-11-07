provider "aws" {
	access_key = "access_key"
	secret_key = "secret_key"
	region = "eu-central-1"
}
resource "aws_instance" "web_server" {
	ami = "ami-0caef02b518350c8b"
	instance_type = "t2.micro"
}
