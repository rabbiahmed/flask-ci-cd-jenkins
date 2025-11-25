# Flask CI/CD with Jenkins 

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
* `flask.service`: The **Systemd** unit file for production-ready deployment.

---

## Jenkinsfile (Pipeline as Code)

The `Jenkinsfile` defines the following stages:

* **Checkout Code:** Clones the repository from GitHub.
* **Build & Dependencies:** Installs Python dependencies including **Gunicorn**.
* **Test (Simulated):** Performs a basic syntax check. *(To be updated with Pytest)*
* **Deploy:** Stops any running instance, copies the `flask.service` Systemd unit file, and starts the application via **Gunicorn** to ensure the process remains running after Jenkins exits.

---

## Deployment Status

The application is deployed and accessible on the Jenkins host on port 5000.

### 1. Successful Pipeline Status

The final build log confirms the successful execution of all stages, including the system service deployment:

```text
[Pipeline] sh
+ sudo /usr/bin/systemctl status flask.service
... (omitted successful enable and daemon-reload steps)
[Pipeline] echo
Application deployed to port 5000 and managed by Systemd!
[Pipeline] End of Pipeline
Finished: SUCCESS
```

### 2. Application Status

The application is successfully running on the server's network address.

Status	    Location	                Port	
Deployed	http://[HOST_IP_ADDRESS]	5000