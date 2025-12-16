# 4Kmovies
A modern Movie Database web application built with React and Tailwind CSS, allowing users to search for movies and view detailed information using the OMDb API.
This project is developed as a Frontend Capstone Project and simulates a real-world frontend development workflow, including API integration, responsive UI design, state management, and deployment.

## Project Overview

- 4Kmovies enables users to:
- Search for movies by title
- View a list of matching movies with posters and release years
- Click on a movie to see detailed information such as plot, cast, genre, and ratings
- Enjoy a clean, responsive experience across desktop and mobile devices

## Tech Stack

- Frontend Framework: React (Vite)
- Styling: Tailwind CSS
 - API: OMDb API
- State Management: React HooK (useState, useEffect)
- Deployment: Netlify / Vercel (planned)

## Features
- Search movie functionality
- Movie listang with posters and basic Info
- Detailed movie view
- Fully responsive web design 
- Error handling for empty results and API failures
- loading indicators for better UX

## State Management

The application uses React hooks to manage state:
- query – user search input
- movies – search results
- selectedMovie – movie details view
- loading – loading state
- error – error message