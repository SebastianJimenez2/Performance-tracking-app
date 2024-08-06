import React, { useState } from 'react';
import { Table, Button, Form } from 'react-bootstrap';
import file from '../assets/file.svg';

function CourseTable() {
  const courses = [
    { id: 1, name: "Curso 1", area: "Mecánica", semester: "2024-A", documentUrl: "url-to-download-document-1.pdf" },
    { id: 2, name: "Curso 2", area: "Economía", semester: "2023-B", documentUrl: "url-to-download-document-2.pdf" },
    { id: 3, name: "Curso 3", area: "Sistemas", semester: "2024-A", documentUrl: "url-to-download-document-3.pdf" }
  ];

  const [selectedSemester, setSelectedSemester] = useState('2024-A'); // Estado para el semestre seleccionado

  const handleDownload = (url: string) => {
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', '');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const filteredCourses = courses.filter(course => course.semester === selectedSemester);

  return (
    <div style={{ maxWidth: '80%', margin: '2rem auto' }}>
      <Form.Select
        aria-label="Selecciona un semestre"
        value={selectedSemester}
        onChange={e => setSelectedSemester(e.target.value)}
        style={{ marginBottom: '20px', width: '15%', justifyContent: 'center' }}
      >
        <option value="2024-A">2024-A</option>
        <option value="2023-B">2023-B</option>
      </Form.Select>
      <Table striped bordered hover className="text-center">
        <thead>
          <tr>
            <th>Capacitación</th>
            <th>Área</th>
            <th>Semestre</th>
            <th>Documento</th>
          </tr>
        </thead>
        <tbody>
          {filteredCourses.map(course => (
            <tr key={course.id}>
              <td>{course.name}</td>
              <td>{course.area}</td>
              <td>{course.semester}</td>
              <td>
                <Button variant="link" onClick={() => handleDownload(course.documentUrl)}>
                  <img src={file} alt="Download" style={{ width: 24, height: 24 }} />
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default CourseTable;
