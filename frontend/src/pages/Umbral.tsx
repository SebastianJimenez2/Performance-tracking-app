import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/pages/Silabo.css'
type UmbralProps = {
    id: string
}

export const Umbral = ({ id }: UmbralProps) => {
    return (
        <div id={id} className='silabo-contenedor'>

            <h1 className='title text-center'>Umbral de comprensión</h1>
            <h2>Verificación y Validación de Software</h2>

            <div className="contenedor-tabla text-center">

                <table className='text-center'>
                    <thead>
                        <tr>
                            <th className='celda-tabla'>Tema</th>
                            <th className='celda-tabla'>Umbral de Comprensión</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr className='no-comprende'>
                            <td className='celda-tabla'>Introducción</td>
                            <td className='celda-tabla'>57%</td>
                        </tr>
                        <tr className='comprende'>
                            <td className='celda-tabla'>Actividades del proceso</td>
                            <td className='celda-tabla'>89%</td>
                        </tr>
                        <tr className='no-comprende'>
                            <td className='celda-tabla'>Error, defecto y fallo</td>
                            <td className='celda-tabla'>32%</td>
                        </tr>
                        <tr className='comprende'>
                            <td className='celda-tabla'>Revisiones</td>
                            <td className='celda-tabla'>90%</td>
                        </tr>
                        <tr>
                            <td className='celda-tabla'>Mejoramiento del proceso</td>
                            <td className='celda-tabla'>Faltan datos</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    )
}

