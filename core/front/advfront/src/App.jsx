import { useState } from 'react'


import './App.css'
import Home from './components/Home'
import Advocatepage from './components/Advocatepage'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
function App() {
  return (
   <Router>
    <Routes>
<Route element={<Home/>} path=''/>
<Route element={<Advocatepage/>} path='/adv/:username'/>
    </Routes>
   </Router>
  )
}

export default App
