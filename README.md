# Monday.com Business Intelligence Agent

## Overview

This application answers founder-level business questions using live data from monday.com boards. It integrates with the monday.com GraphQL API, cleans messy board data, and computes business insights in real time.

Every query triggers a live API call. No caching or preloading is used.

---

## Problem Statement

Founders and executives often need quick answers to questions such as:

- How is our pipeline looking?
- Which sector is generating the most revenue?
- How many closed deals resulted in work orders?

Manually answering these requires extracting data from multiple boards, cleaning inconsistent formats, and performing ad-hoc analysis. This agent automates that process.

---

## Architecture

User Question
↓
Query Interpretation
↓
Live monday.com API Call
↓
Data Cleaning
↓
Business Logic Computation
↓
Insight Output

---

## Boards Used

### Deal Funnel Data Structure
Board ID: 5026932277  

### Work Order Tracker Structure
Board ID: 5026934474  

### API Endpoint
https://api.monday.com/v2  

---

## Features

- Live monday.com API integration  
- No caching (live fetch per query)  
- Handles messy and inconsistent data  
- Natural language query interpretation  
- Sector-level and pipeline analytics  
- Visible API/tool-call trace  

---

## Tech Stack

- Python 3.11  
- Streamlit  
- OpenAI API  
- monday.com GraphQL API  
- Pandas  
- python-dotenv  

---

## Project Structure

monday_agent/
├── app.py
├── monday_api.py
├── agent.py
├── data_cleaning.py
├── business_logic.py

### Create Environment
conda create -n monday_agent python=3.11
conda activate monday_agent

### Install Dependencies
pip install -r requirements.txt
### Create `.env` File
MONDAY_API_KEY=your_monday_api_key
OPENAI_API_KEY=your_openai_api_key

### Run the Application
streamlit run app.py

---

## Example Queries

- How is the energy sector pipeline?
- Show total pipeline value by sector.
- What is the average deal size?
- How many deals converted to work orders?

---

## Design Decisions

- Python was chosen for strong API and AI ecosystem support.  
- Streamlit was selected for rapid development and easy deployment.  
- GraphQL enables efficient board data retrieval.  
- Live API execution ensures real-time insights.  

---

## Deployment

Hosted on Streamlit Cloud.
