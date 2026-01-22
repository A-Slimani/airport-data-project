terraform {
    required_providers {
        google = {
            source = "hashicorp/google"
        }
    }
}

provider "google" {
    project = "airport-dataeng"
    region = "australia-southeast1"
}

resource "random_id" "bucket_suffix" {
    byte_length = 4
}

resource "google_storage_bucket" "raw_flight_data" {
    name = "raw_flight_data-${random_id.bucket_suffix.hex}"
    location = "australia-southeast1"
    force_destroy = true
}