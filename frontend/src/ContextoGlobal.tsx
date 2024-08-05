import { createContext, useState, ReactNode, useContext } from 'react'

type contextoType = {
    paginaActual: string;
    setPaginaActual: (paginaActual: string) => void;
}

const ContextoGlobal = createContext<contextoType | undefined>(undefined)

export function ProveedorContextoGlobal({ children }: { children: ReactNode }) {
    const [paginaActual, setPaginaActual] = useState<string>('')

    return (
        <ContextoGlobal.Provider value={{ paginaActual, setPaginaActual }}>
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