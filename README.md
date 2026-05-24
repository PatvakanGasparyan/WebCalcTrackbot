# WebCalcTrackbot 💱

This is a user-friendly Telegram bot for real-time currency conversion. The bot not only calculates currency rates but also saves the complete request history to a database. A dedicated website allows the owner to view this history in a clean table format.

---

## 🚀 Key Features

* **Fast Calculation**: The user sends a message to the bot (e.g., `100 USD EUR`), and the bot instantly replies with the result based on fresh exchange rates.
* **History Logging**: All user actions are automatically saved into a MySQL database.
* **Web Dashboard (Admin Panel)**: A simple Flask-based website that displays a table containing all past conversions.

---

## 🏗 Project Architecture

The diagram below shows how different parts of the application communicate with each other:

```mermaid
graph TD;
    User[User] -->|1. Sends: 100 USD EUR| Bot[Telegram Bot]
    Bot -->|2. Requests rate| API[Currency Exchange API]
    Bot -->|3. Sends result| User
    Bot -->|4. Saves log| DB[(MySQL Database)]
    WebSite[Flask Website] -->|5. Reads history| DB
    Admin[Bot Owner] -->|6. Views table| WebSite
