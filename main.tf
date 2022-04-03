terraform {
  required_version = "~> 1.0.0"

  backend "gcs" {
    prefix  = "terraform/state"
//    bucket  = "" #these will be passed as backend-config variables in the terraform init. See cloubuild.yaml.
//    project = ""
  }
}

provider "google" {
  project     = "${var.project-name}"
  region      = "${var.region}"
}

variable "project-name" {
  type    = "string"
}

variable "region" {
  type    = "string"
  default = "us-east1-d"
}

variable "image" {
  type    = "string"
  default = "gcr.io/google-samples/hello-app:1.0"
}

variable "app_name" {
  type    = "string"
  default = "api"
}

resource "google_project_service" "run_api" {
  service = "run.googleapis.com"

  disable_on_destroy = true
}

# main.tf

# Create the Cloud Run service
resource "google_cloud_run_service" "run_service" {
  name = "${var.app_name}"
  location = "${var.region}"

  template {
    spec {
      containers {
        image = "${var.image}"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

  # Waits for the Cloud Run API to be enabled
  depends_on = [google_project_service.run_api]
}

resource "google_cloud_run_service_iam_member" "run_all_users" {
  service  = google_cloud_run_service.run_service.name
  location = google_cloud_run_service.run_service.location
  role     = "roles/run.invoker"
  member   = "allUsers"
}

output "service_url" {
  value = google_cloud_run_service.run_service.status[0].url
}
