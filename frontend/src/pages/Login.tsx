/**
 * Creado por: David Torres
 */
import { useState, FormEvent } from 'react';
import { useContextoGlobal } from '../ContextoGlobal';
import '../styles/pages/Login.css';

const Login = () => {
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const { setPaginaActual, setRol,setUsuario } = useContextoGlobal(); // Hook para actualizar la página actual

  const handleLogin = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault(); // Prevent form from refreshing the page

    // Validar campos
    if (!email || !password) {
      alert('Complete ambos campos para iniciar sesión.');
      return;
    }

    if(email == "admin@epn.edu.ec"){
      setRol('administrador')
      setUsuario('Administrador')
      setPaginaActual('Home');
    }else{
      setRol('docente')
      setUsuario('Mario Romero')
      setPaginaActual('Cursos');
    }

  };

  return (
    <div className="login-container">
      <div className="bg-image"></div>
      <div className="form-container">
        <form className="login-form" onSubmit={handleLogin}>
          <h1 className="login-title">Bienvenido</h1>
          <h2 className="login-subtitle">Inicia sesión</h2>
          <div className="input-group">
            <label htmlFor="email" className="input-label">
              Usuario
            </label>
            <input
              id="email"
              type="email"
              placeholder="email@epn.edu.ec"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="input-field"
            />
          </div>
          <div className="input-group">
            <label htmlFor="password" className="input-label">
              Contraseña
            </label>
            <input
              id="password"
              type="password"
              placeholder="********"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="input-field"
            />
          </div>
          <button type="submit" className="submit-button">
            Ingresar
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
