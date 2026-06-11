# Security Log Analyzer

## Project Overview
This project uses Python and SQLite to analyze login events and identify IP addresses with repeated failed login attempts.

## Features
- Reads login data from a CSV file
- Stores events in a SQLite database
- Detects repeated failed login attempts
- Uses SQL to summarize suspicious activity
- Handles UTF-8 encoded text

## Technologies Used
- Python
- SQL
- SQLite
- CSV
- UTF-8 encoding

## Detection Rule
An IP address is marked as suspicious when it generates three or more failed login attempts.

## How It Works
1. Python reads the CSV file of login events.
2. Each login event is inserted into a SQL table.
3. The program counts failed attempts by IP address.
4. IP addresses meeting the detection rule are displayed.

## Example Output
Example output is showcased in `security-log-analyzer/screenshots`

## Security Relevance
Repeated failed login attempts can indicate:
- Attacks such as brute-force
- Password guessing
- Credential-stuffing attempts
- Misconfigured applications

## What I Learned
- How programs process and represent data
- How UTF-8 encoding handles text
- How Python reads files such as CSV
- How SQL stores and retreives information via tables and queries
- How simple detection rules can identify suspicious behavior

## References
- TryHackMe. "Introduction to Cyber Security." TryHackMe, [https://tryhackme.com/](https://tryhackme.com/module/software-basics)

## Disclaimer
This project is for educational purposes only. It summarizes concepts learned through TryHackMe and does not include walkthrough answers, flags, or private room solutions.