import React from 'react';
import BarraNavegacion from '../components/BarraNavegacion';
import Cards from '../components/Cards.tsx';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/pages/Cursos.css';

const Cursos = () => {
    return (
        <div className='cursos-container'>
            <BarraNavegacion />
            <main className='main-content d-flex justify-content-center align-items-center px-5'>
                <div>
                <h1 className='cursos-title'><strong>Cursos</strong></h1>
                    <Cards />
                </div>
            </main>
        </div>
    );
};

export default Cursos;
