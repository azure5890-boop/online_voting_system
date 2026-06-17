# Online Voting System

## Overview

The Online Voting System is a Python-based console application that simulates an election process. The system allows citizens to register, become voters, apply as candidates, and participate in elections. Administrators can manage candidate approvals and oversee the election process.

## Features

### Citizen Management

* Citizen Registration
* National ID Verification
* Phone Number Validation
* Age Verification

### Voter Management

* Voter Registration
* Voter Login
* Unique Voter Code Generation
* Voter Authentication
* Vote Tracking

### Candidate Management

* Candidate Registration
* Candidate Approval Workflow
* Candidate Rejection Workflow
* Candidate Status Management

### Admin Management

* Admin Login
* Role-Based Access Control
* Candidate Approval/Rejection
* Election Monitoring
* Result Management

### Database Features

* MySQL Database Integration
* Foreign Key Relationships
* Data Validation
* Secure Record Management

---

## Project Structure

```text
online_voting_system/
│
├── admin/
│   ├── admin_login.py
│   ├── admin_menu.py
│   ├── approve_candidate.py
│   └── results.py
│
├── candidate/
│   ├── candidate_register.py
│   └── candidate_status.py
│
├── citizen/
│   └── citizen_register.py
│
├── database/
│   ├── db_connect.py
│   └── schema.sql
│
├── utils/
│   ├── id_generator.py
│   ├── validators.py
│   └── voter_code.py
│
├── voter/
│   ├── voter_register.py
│   ├── voter_login.py
│   └── cast_vote.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Database Schema

### Tables

* citizens
* voters
* candidates
* votes
* admins

### Relationships

* A citizen can become a voter.
* A citizen can apply as a candidate.
* A voter can cast only one vote.
* Admins manage candidate approvals and election operations.

---

## Technologies Used

* Python 3
* MySQL
* mysql-connector-python

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd online_voting_system
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

### Activate Virtual Environment

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

1. Start MySQL Server.
2. Create a database.
3. Execute the `schema.sql` file.

```bash
mysql -u root -p < database/schema.sql
```

### Configure Database Connection

Update `database/db_connect.py` with your MySQL credentials.

```python
host="localhost"
user="root"
password="your_password"
database="election_system"
```

---

## Running the Application

```bash
python main.py
```

---

## Admin Roles

### Super Admin

Privileges:

* View Pending Candidates
* Approve Candidates
* Reject Candidates
* View Results
* Manage Election Process

---

## Validation Rules

### Citizen Registration

* National ID must be unique.
* Phone number must be unique.
* Gender must be M or F.

### Voter Registration

* Citizen must exist.
* Age must be at least 18.
* Citizen cannot register twice as a voter.

### Candidate Registration

* Citizen must exist.
* Age must be at least 18.
* Candidate cannot register twice.

---

## Future Improvements

* Password Hashing
* Election Start/End Dates
* Candidate Profile Information
* Multiple Admin Roles
* Graphical User Interface (GUI)
* Web-Based Voting Portal
* Audit Logs
* Email/SMS Verification

---

## Author

Developed as a learning project for understanding:

* Python Programming
* MySQL Databases
* Authentication Systems
* Role-Based Access Control
* Database Design
* Software Development Practices

```
```
