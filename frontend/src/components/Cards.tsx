import React from 'react';
import { useContextoGlobal } from '../ContextoGlobal'; // Asegúrate de importar el contexto
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/components/Cards.css';

const Cards = () => {
    const { setPaginaActual } = useContextoGlobal(); // Obtén el setter del contexto

    const irAEstudiantes = () => {
        setPaginaActual('Estudiantes'); // Cambia la página actual en el contexto
    };

    return (
        <div className="card-container">
            {/* Verificación y Validación */}
            <div className='card'>
                <h3 className='card-title'>Verificación y Validación</h3>
                <img src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjix6X90r95gsEVpT5Q-5J4Nx_t-SIYdc9H8a6BfSv1n2-xModsa3YClW6m9UEVTCTyYga2G3wopItUx-b_YTnQbMSciSJ_Silj8FL7Cgk_LJ_ZT_YnD2ar20HKelTUlGNE2U3ZXGb5I-ER/s1600/screenshot_2020-03-17-11-21-55-77.jpg' alt='Card 1' className='card-image' />
                <button className='card-button' onClick={irAEstudiantes}>Acceder</button>
            </div>
        </div>
    );
};

export default Cards;