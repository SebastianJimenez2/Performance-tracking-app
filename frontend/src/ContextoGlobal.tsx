import { createContext, useState, ReactNode, useContext } from 'react'
import { Profesor } from './types/Capacitaciones';

type contextoType = {
    paginaActual: string;
    setPaginaActual: (paginaActual: string) => void;
    profesor: Profesor | null; 
    setProfesor: (profesor: Profesor | null) => void; 
    modoUsuario: string; 
    setModoUsuario: (modo: string) => void; 
}

const ContextoGlobal = createContext<contextoType | undefined>(undefined)

export function ProveedorContextoGlobal({ children }: { children: ReactNode }) {
    const [paginaActual, setPaginaActual] = useState<string>('')
    const [profesor, setProfesor] = useState<Profesor | null>(null);
    const [modoUsuario, setModoUsuario] = useState<string>('normal');

    return (
        <ContextoGlobal.Provider value={{ paginaActual, setPaginaActual,profesor, setProfesor, modoUsuario, setModoUsuario }}>
            {children}
        </ContextoGlobal.Provider>
    )
}

export function useContextoGlobal() {
    const contexto = useContext(ContextoGlobal)
    
    if (contexto === undefined) {
        throw new Error('useGlobalContext must be used within a GlobalContextProvider')
    }
    
    return contexto
}