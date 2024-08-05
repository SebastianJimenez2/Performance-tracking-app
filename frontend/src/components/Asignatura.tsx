import Tabs from './Tabs';
import BarraNavegacion from './BarraNavegacion';

type AsignaturaProps = {
    children: React.ReactNode[];
}

function Asignatura({ children }: AsignaturaProps) {

    return (
        <>
            <BarraNavegacion />
            <Tabs>
                {children}
            </Tabs>
        </>
    )
}

export default Asignatura
