import { createContext, useState, ReactNode, useContext } from 'react'
import { Estudiante } from './types/RegistroNotas';

type contextoType = {
    paginaActual: string;
    setPaginaActual: (paginaActual: string) => void;
    listaEstudiantes: Estudiante[];
    setListaEstudiantes: (listaEstudiantes: Estudiante[]) => void;
}

const ContextoGlobal = createContext<contextoType | undefined>(undefined)

export function ProveedorContextoGlobal({ children }: { children: ReactNode }) {
    const [paginaActual, setPaginaActual] = useState<string>('Asignatura')
    const [listaEstudiantes, setListaEstudiantes] = useState<Estudiante[]>([])

    return (
        <ContextoGlobal.Provider value={{ paginaActual, setPaginaActual, listaEstudiantes, setListaEstudiantes }}>
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
