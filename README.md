# 🚌 Redbus Data Scraping & Dynamic Filtering App using Streamlit

![Web Scraping](https://img.shields.io/badge/Web%20Scraping-Selenium-blue)
![Frontend](https://img.shields.io/badge/UI-Streamlit-green)
![Database](https://img.shields.io/badge/SQL-Integrated%20Database-lightgrey)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## 📘 Project Overview

This project extracts live bus travel data from **Redbus** (routes, prices, schedules, seat availability) using **Selenium** and stores it in a **SQL database**. A sleek **Streamlit web app** then lets users filter and explore the data interactively.

---

## 🎯 Objective

- 🔍 Scrape real-time data from Redbus website
- 🧠 Store data in a structured format (SQL DB)
- 🖥️ Display it dynamically in an interactive **Streamlit** app
- 🧳 Help users and travel agencies make **better travel decisions**

---

## 🧠 Approach

### 1️⃣ Web Scraping with Selenium
- Extracts:
  - 🚌 Route info (from → to)
  - ⏱️ Departure & Arrival times
  - 💺 Seat availability
  - 💵 Price
  - ⭐ Ratings
- Handles dynamic elements & JavaScript rendering
- Error handling & page navigation automated

### 2️⃣ Data Storage in SQL
- Structured storage in **SQLite / MySQL**  
- Columns: `bus_name`, `departure_time`, `arrival_time`, `price`, `route`, `seats_available`, `rating`
- Enables efficient querying and real-time updates

### 3️⃣ Streamlit-Based Interactive Filtering App
- User-friendly web UI to explore scraped data
- 🔎 Filters:
  - Bus type (AC/Non-AC, Sleeper, Volvo)
  - Price range slider
  - Source/Destination route filter
  - Ratings & seat availability
- SQL queries fetch and display only relevant results

---

## 🖼️ Streamlit App Preview

> Search. Filter. Compare. Choose.  
Your personal Redbus assistant built with **Python + Selenium + SQL + Streamlit**.

✅ View only available buses  
✅ Sort by rating or price  
✅ Filter by custom routes and travel types  
✅ Simple UI for complex filtering logic

---
