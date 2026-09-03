// frontend/src/components/StakeholdersList.tsx

import { useEffect, useState } from 'react';
import api from '../services/api';
import { Stakeholder } from '../types/iniciacao';

export function StakeholdersList() {
  const [stakeholders, setStakeholders] = useState<Stakeholder[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    api.get<Stakeholder[]>('/iniciacao/stakeholders/')
      .then((response) => {
        setStakeholders(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Erro ao carregar stakeholders:', error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Carregando stakeholders...</p>;

  return (
    <div style={{ padding: '20px' }}>
      <h2>Módulo 1: Stakeholders do Projeto</h2>
      {stakeholders.length === 0 ? (
        <p>Nenhum stakeholder cadastrado ainda.</p>
      ) : (
        <ul>
          {stakeholders.map((item) => (
            <li key={item.id} style={{ marginBottom: '10px' }}>
              <strong>{item.nome}</strong> - {item.cargo} ({item.departamento}) | <em>{item.email}</em>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}