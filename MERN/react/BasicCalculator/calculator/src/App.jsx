import { useState } from 'react'
import Calculate from './Calculatorcomponent'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Calculate />
      
    </>
  )
}

export default App
