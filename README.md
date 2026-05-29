# DreamTimetable IIT - Professional Edition

> A highly sophisticated, AI-powered academic scheduling platform built for IIT Bombay, featuring automated conflict resolution, facial verification, and enterprise-grade infrastructure.

## 🚀 Key Features

* **AI Constraint Engine**: Utilizes advanced optimization algorithms to solve complex scheduling matrices involving faculty preferences, senate limits, student choices, and infrastructure constraints.
* **Modern Dashboard**: Built with Next.js, React, Tailwind CSS, and ShadCN for a beautiful, responsive user experience.
* **Facial Verification (FaceAuth)**: Secures critical administrative actions (generation, export) using `face-api.js` local AI models.
* **Data Persistence**: Uses a local SQLite database for storing timetables, user data, and tracking analytics history securely.
* **Advanced Analytics**: Visualizes infrastructure utilization and faculty teaching loads via Recharts.
* **Desktop Application**: Packaged via Electron for a native Windows executable experience with no installation overhead.
* **Export Engine**: Generates professional PDF and Excel reports for administration and faculty.

## 🛠️ Technology Stack

* **Frontend**: Next.js 15 (App Router), React 19, Tailwind CSS v4, Lucide React
* **AI Engine**: TypeScript, Zod, face-api.js
* **Backend / Desktop**: Electron, better-sqlite3, Node.js
* **Data Visualization**: Recharts

## 📦 Project Architecture

```
/app                 - Next.js application routes (Dashboard, Generator, Analytics, etc.)
/components          - Reusable React components (TimetableGrid, UI elements)
/face-verification   - Face API authentication modules
/timetable-engine    - The core scheduling logic (ConstraintEngine, Models, MockData)
/database            - SQLite setup and schema definitions
/services            - Local storage and API interactions
/exports             - Export handlers for PDF and Excel
main.js              - Electron entry point
```

## ⚙️ Installation & Usage

### 1. Prerequisites
Ensure you have Node.js (v20+) installed.

### 2. Install Dependencies
```bash
npm install
```

### 3. Run Development Server
```bash
npm run dev
```

### 4. Build Desktop Application (Windows .exe)
```bash
npm run electron:build
```
The compiled executable will be located in the `dist-electron/` directory.

## 🔒 Security
The platform uses **local, on-device facial recognition**. No biometric data leaves the system.

---
*Developed for professional showcase and enterprise-level scheduling.*
