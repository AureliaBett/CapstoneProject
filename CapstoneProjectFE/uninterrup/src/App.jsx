import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import AppLayout from "./layouts/AppLayout";
import Homepage from "./pages/Homepage";
import Dashboard from "./pages/Dashboard";


export default function App() {
  return (
    <BrowserRouter>
      <AppLayout>
        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </AppLayout>
    </BrowserRouter>
  );
}