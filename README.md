# Flask CI/CD with Jenkins 

[![Build Status](https://your-jenkins-instance/build-status-badge-link)](https://your-jenkins-instance/)

This project demonstrates a complete Continuous Integration/Continuous Deployment (CI/CD) pipeline for a simple Python **Flask** web application using **Jenkins** running on an Ubuntu server.

---

## Architecture and Flow

The pipeline is triggered by a Git push, automating the process from code commit to live deployment.

**The Workflow:**
1. Developer pushes code to the **main** branch on GitHub.
2. Jenkins detects the change via the GitHub hook trigger.
3. The Pipeline executes the defined stages: **Checkout**, **Build**, **Test**, and **Deploy**.
4. The application is deployed and made available on port 5000.

---

## Getting Started

### Prerequisites

The following software must be installed on the Linux host running Jenkins:
* Ubuntu 22.04+
* Java 21 LTS
* Jenkins LTS
* Python 3.x and pip

### Application Files

The repository contains:
* `app.py`: The basic Flask application code.
* `requirements.txt`: Specifies the `Flask` dependency.
* `Jenkinsfile`: The declarative Pipeline definition.

---

## Jenkinsfile (Pipeline as Code)

* `Jenkinsfile`: The declarative Pipeline definition.