terraform {
  cloud {
    organization = "example-org-4fbde8"

    workspaces {
      name = "learn-terraform-github-actions"
    }
  }
}