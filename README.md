# Cloud Computing Project 3 – Azure SQL Database

## Overview

This project was completed during my Cloud Computing (AWS/Azure) Internship at DecodeLabs.

The objective was to provision a managed cloud database, create a relational schema, populate it with sample records, and retrieve the data programmatically using Python.

---

## Technologies

- Microsoft Azure
- Azure SQL Database
- SQL
- Python
- pyodbc
- Azure Portal

---

## Architecture

Python Application
        │
        ▼
pyodbc Driver
        │
        ▼
Azure SQL Database
        │
        ▼
Interns Table
        │
        ▼
SELECT Query
        │
        ▼
Console Output

---

## Features

- Provisioned Azure SQL Database
- Designed relational schema
- Created Interns table
- Inserted multiple records
- Queried database using SQL
- Connected using Python
- Retrieved cloud-hosted data

---

## Database Schema

| Column | Type |
|----------|------------|
| ID | INT |
| Name | NVARCHAR(100) |
| Role | NVARCHAR(100) |
| Email | NVARCHAR(255) |

---

## SQL Operations

- CREATE TABLE
- INSERT
- SELECT

---

## Python Connectivity

Python connects securely to Azure SQL Database using pyodbc and retrieves all stored records.

---

## Learning Outcomes

✔ Azure SQL Database

✔ Cloud Database Provisioning

✔ Relational Database Design

✔ SQL Queries

✔ Python Database Connectivity

✔ Cloud Security Basics

✔ Managed Database Services

---

## Screenshots

Included inside the screenshots folder.

---

Developed during the DecodeLabs Cloud Computing Internship.
