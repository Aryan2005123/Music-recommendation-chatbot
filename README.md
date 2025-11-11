# Music & Movie Recommendation System (Combined Project)

## Overview
This is a starter template for a combined music and movie recommendation system.
It includes:
- A simple content-based + collaborative filtering recommender (Python).
- A small sample dataset (placeholder).
- A Flask API exposing recommendation endpoints.
- Jupyter notebook demonstration.
- Instructions to run in VS Code.

## Quick start (VS Code)
1. Open this folder in VS Code.
2. Create and activate a Python virtual environment:
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r src/requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python src/app.py
   ```
   The API will be available at http://127.0.0.1:5000

## Example endpoints
- `GET /recommend/movies/user/<user_id>` -> movie recommendations for a user
- `GET /recommend/music/user/<user_id>` -> music recommendations for a user
- `GET /recommend/movies/content/<item_id>` -> content-based similar movies
- `GET /recommend/music/content/<item_id>` -> content-based similar songs

## Notes
- This is a template with small sample datasets. Replace with real datasets (e.g., MovieLens, Spotify data) for production usage.
- For better performance and accuracy, use matrix factorization (e.g., implicit ALS), and larger datasets.
