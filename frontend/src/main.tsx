import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import { ProveedorContextoGlobal } from './ContextoGlobal.tsx'

import './styles/index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <ProveedorContextoGlobal>
    <React.StrictMode>
      <App />
    </React.StrictMode>
  </ProveedorContextoGlobal>
)
