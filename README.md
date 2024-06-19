# MULTIOMICS DB

[![image](https://github.com/bihealth/sodar-server/actions/workflows/build.yml/badge.svg)](https://github.com/bihealth/sodar-server/actions/workflows/build.yml)

[![image](https://coveralls.io/repos/github/bihealth/sodar-server/badge.svg?branch=main)](https://coveralls.io/github/bihealth/sodar-server?branch=main)

[![image](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

[![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This is a specialized system for managing data in omics research
projects. It provides biomedical scientists with a single point of
access to data in their projects, along with linking out to external
resources and systems.

Main features are:

-   Project based access control and data encapsulation
-   Modeling study design metadata
-   Large scale data storage
-   Linking files to metadata
-   Validation of file uploads
-   Various tools for aiding in data management

The project is built on the [SODAR
Core](https://github.com/bihealth/sodar-core) framework, which provides
the base functionalities for project management, user interfaces and
dynamic app content inclusion. See the [SODAR Overview video on
YouTube](https://www.youtube.com/watch?v=LQ8foUpjnqs) for an
introduction to the SODAR system and its features.

Django apps provided by SODAR:

-   **Samplesheets**: Modeling of study metadata in the ISA-Tab format
-   **Landingzones**: Management of file validation and uploads into
    iRODS
-   **Irodsadmin**: iRODS data administration helpers
-   **Irodsbackend**: Backend app for iRODS queries and operations
-   **Irodsinfo**: Display iRODS server information and create user
    configurations
-   **Ontologyaccess**: Parse, store and serve ontologies for local
    lookup
-   **Taskflowbackend**: Run iRODS transactions with full rollback for
    project and file operations

Getting Started
===============

For instructions on using and administering the system, see the [SODAR
manual](https://sodar-server.readthedocs.io/).

For trying out the system or deploying it in production, see the [SODAR
Docker Compose](https://github.com/bihealth/sodar-docker-compose)
repository.

Technical Information
=====================

This project provides a web-based GUI and REST APIs running on the
[Django](https://www.djangoproject.com/) web server.

Studies are modeled with the [ISA Model](https://isa-tools.org)
specification. For file storage SODAR uses the
[iRODS](https://irods.org/) open source data management software.
