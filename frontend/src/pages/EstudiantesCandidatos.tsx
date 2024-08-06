type EstudiantesCandidatosProps = {
        id: string
}

function EstudiantesCandidatos({ id }: EstudiantesCandidatosProps) {
        return (
                <div>
                        <h1> {id}</h1>
                </div>
        );
}

export default EstudiantesCandidatos;
