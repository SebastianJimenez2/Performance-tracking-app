import { createContext, useState, ReactNode, useContext } from 'react'
import { Estudiante } from './types/Estudiantes';
import { Profesor } from './types/Capacitaciones';


type contextoType = {
    paginaActual: string;
    setPaginaActual: (paginaActual: string) => void;
    listaEstudiantes: Estudiante[];
    setListaEstudiantes: (listaEstudiantes: Estudiante[]) => void;
    profesor: Profesor | null;
    setProfesor: (profesor: Profesor | null) => void;
    rol: string;
    setRol: (modo: string) => void;
    usuario: string;
    setUsuario: (usuario: string) => void;
    asignatura: number;
    setAsignatura: (asignatura: number) => void;
    curso: number;
    setCurso: (curso: number) => void;
    periodoActivo: number;
    setPeriodoActivo: (periodoActivo: number) => void;
    mostrarCampana: boolean;
    setMostrarCampana: (mostrar: boolean) => void;
}

const ContextoGlobal = createContext<contextoType | undefined>(undefined)

export function ProveedorContextoGlobal({ children }: { children: ReactNode }) {
    const [paginaActual, setPaginaActual] = useState<string>('')
    const [listaEstudiantes, setListaEstudiantes] = useState<Estudiante[]>([])
    const [profesor, setProfesor] = useState<Profesor | null>(null);
    const [rol, setRol] = useState<string>('');
    const [usuario, setUsuario] = useState<string>('');
    const [asignatura, setAsignatura] = useState<number>(0);
    const [curso, setCurso] = useState<number>(0);
    const [periodoActivo, setPeriodoActivo] = useState<number>(6);
    const [mostrarCampana, setMostrarCampana] = useState<boolean>(false);

    return (
        <ContextoGlobal.Provider value={{
            paginaActual, setPaginaActual, listaEstudiantes, setListaEstudiantes, profesor, setProfesor,
            rol, setRol, usuario, setUsuario, asignatura, setAsignatura, curso, setCurso,
            periodoActivo, setPeriodoActivo, mostrarCampana, setMostrarCampana
        }}>
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
